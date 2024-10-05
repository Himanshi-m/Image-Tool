import streamlit as st
from PIL import Image, ImageEnhance
from io import BytesIO
from streamlit_cropper import st_cropper
from rembg import remove
import base64
import cv2
import numpy as np
from concurrent.futures import ThreadPoolExecutor
import zipfile

# Initialize session state for navigation
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# Function to navigate to a different page
def navigate_to(page):
    st.session_state.page = page

# Function to convert PIL image to base64
def pil_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Function to clean up borders using OpenCV
def clean_borders(image):
    open_cv_image = np.array(image)
    b, g, r, a = cv2.split(open_cv_image)
    mask = a.copy()
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    mask = np.zeros_like(a)
    cv2.drawContours(mask, contours, -1, 255, thickness=cv2.FILLED)
    new_image = cv2.merge([b, g, r, mask])
    return Image.fromarray(new_image, 'RGBA')

# Function to resize image while maintaining aspect ratio
def resize_image(image, target_width=None, target_height=None):
    original_width, original_height = image.size
    if target_width and target_height:
        aspect_ratio = original_width / original_height
        if target_width / target_height > aspect_ratio:
            target_width = int(target_height * aspect_ratio)
        else:
            target_height = int(target_width / aspect_ratio)
    elif target_width:
        target_height = int(target_width / (original_width / original_height))
    elif target_height:
        target_width = int(target_height * (original_width / original_height))
    else:
        return image
    return image.resize((target_width, target_height), Image.LANCZOS)

# Set up the main window
st.title("Image Manipulation Tool")

# Menu bar
menu = st.sidebar.selectbox("Menu", ["Home", "Resize Image", "Convert Image", "Crop Image", "Enhance Image", "Bulk Background Remover", "Help"], index=["Home", "Resize Image", "Convert Image", "Crop Image", "Enhance Image", "Bulk Background Remover", "Help"].index(st.session_state.page))

# Home Page
if menu == "Home":
    st.header("Welcome to the Image Manipulation Tool!")
    st.write("""
        This tool allows you to perform various image manipulation tasks including resizing, converting, cropping, and enhancing images. 
        Use the navigation menu on the left to access different functionalities.
    """)
    
    # Create a grid for navigation
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Resize Image")
        st.write("Resize your images by specifying dimensions or percentage.")
        if st.button("Go to Resize Image"):
            navigate_to("Resize Image")
    
    with col2:
        st.subheader("Convert Image")
        st.write("Convert your images to different formats.")
        if st.button("Go to Convert Image"):
            navigate_to("Convert Image")
    
    with col3:
        st.subheader("Crop Image")
        st.write("Crop your images to custom dimensions.")
        if st.button("Go to Crop Image"):
            navigate_to("Crop Image")
    
    col4, col5, col6 = st.columns(3)
    
    with col4:
        st.subheader("Enhance Image")
        st.write("Adjust brightness, contrast, and saturation of your images.")
        if st.button("Go to Enhance Image"):
            navigate_to("Enhance Image")
    
    with col5:
        st.subheader("Bulk Background Remover")
        st.write("Remove backgrounds from multiple images at once.")
        if st.button("Go to Bulk Background Remover"):
            navigate_to("Bulk Background Remover")
    
    with col6:
        st.subheader("Help")
        st.write("Get help and information about how to use this tool.")
        if st.button("Go to Help"):
            navigate_to("Help")

# Resize Image Page
elif menu == "Resize Image":
    st.header("Resize Image")
    
    # File uploader
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"], help="Upload an image file to resize.")
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        
        # Resize options
        resize_option = st.radio("Resize Option", ("By Dimensions", "By Percentage"), help="Choose how you want to resize the image.")
        
        if resize_option == "By Dimensions":
            width = st.number_input("Width", value=image.width, help="Enter the new width for the image.")
            height = st.number_input("Height", value=image.height, help="Enter the new height for the image.")
        else:
            percentage = st.number_input("Percentage", value=100, help="Enter the percentage to scale the image.")
            width = int(image.width * (percentage / 100))
            height = int(image.height * (percentage / 100))
        
        if st.button("Resize", help="Click to resize the image."):
            progress = st.progress(0)
            resized_image = resize_image(image, target_width=width, target_height=height)
            progress.progress(50)
            
            # Estimate file size
            buffer = BytesIO()
            resized_image.save(buffer, format="PNG")
            estimated_size = len(buffer.getvalue()) / 1024  # in KB
            st.write(f"Estimated file size: {estimated_size:.2f} KB")
            
            # Display images side by side
            col1, col2 = st.columns(2)
            with col1:
                st.image(image, caption='Uploaded Image', use_column_width=True)
            with col2:
                st.image(resized_image, caption='Resized Image', use_column_width=True)
            
            # Provide a download button
            buffer.seek(0)
            st.download_button(
                label="Download Resized Image",
                data=buffer,
                file_name="resized_image.png",
                mime="image/png",
                help="Click to download the resized image."
            )
            st.success("Image ready for download")
            progress.progress(100)

# Convert Image Page
elif menu == "Convert Image":
    st.header("Convert Image")
    
    # File uploader
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "bmp", "gif", "tiff", "webp", "ico"], help="Upload an image file to convert.")
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        
        # Format selection
        format_option = st.selectbox("Select Output Format", ["JPEG", "PNG", "BMP", "GIF", "TIFF", "WEBP", "ICO"], help="Choose the output format for the image.")
        
        # Quality adjustment for all formats
        quality = st.slider("Quality", 1, 100, 100, help="Adjust the quality of the output image.")
        
        if st.button("Convert", help="Click to convert the image."):
            progress = st.progress(0)
            buffer = BytesIO()
            image.save(buffer, format=format_option, quality=quality)
            buffer.seek(0)
            progress.progress(50)
            
            # Estimate file size
            estimated_size = len(buffer.getvalue()) / 1024  # in KB
            st.write(f"Estimated file size: {estimated_size:.2f} KB")
            
            # Display images side by side
            col1, col2 = st.columns(2)
            with col1:
                st.image(image, caption='Uploaded Image', use_column_width=True)
            with col2:
                st.image(buffer, caption=f'Converted Image ({format_option})', use_column_width=True)
            
            # Provide a download button
            st.download_button(
                label="Download Converted Image",
                data=buffer,
                file_name=f"converted_image.{format_option.lower()}",
                mime=f"image/{format_option.lower()}",
                help="Click to download the converted image."
            )
            st.success("Image ready for download")
            progress.progress(100)

# Crop Image Page
elif menu == "Crop Image":
    st.header("Crop Image")
    
    # File uploader
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"], help="Upload an image file to crop.")
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        
        # Aspect ratio options
        aspect_ratio = st.selectbox("Aspect Ratio", ["Freeform", "1:1", "4:3", "16:9"], help="Choose the aspect ratio for cropping.")
        aspect_dict = {"Freeform": None, "1:1": (1, 1), "4:3": (4, 3), "16:9": (16, 9)}
        
        # Crop the image
        progress = st.progress(0)
        cropped_image = st_cropper(image, aspect_ratio=aspect_dict[aspect_ratio], box_color='blue', return_type='image')
        progress.progress(50)
        
        # Display images side by side
        col1, col2 = st.columns(2)
        with col1:
            st.image(image, caption='Uploaded Image', use_column_width=True)
        with col2:
            st.image(cropped_image, caption='Cropped Image', use_column_width=True)
        
        # Provide a download button
        buffer = BytesIO()
        cropped_image.save(buffer, format="PNG")
        buffer.seek(0)
        st.download_button(
            label="Download Cropped Image",
            data=buffer,
            file_name="cropped_image.png",
            mime="image/png",
            help="Click to download the cropped image."
        )
        st.success("Image ready for download")
        progress.progress(100)

# Enhance Image Page
elif menu == "Enhance Image":
    st.header("Enhance Image")
    
    # File uploader
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"], help="Upload an image file to enhance.")
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        
        # Enhancement options
        brightness = st.slider("Brightness", 0.1, 2.0, 1.0, help="Adjust the brightness of the image.")
        contrast = st.slider("Contrast", 0.1, 2.0, 1.0, help="Adjust the contrast of the image.")
        saturation = st.slider("Saturation", 0.1, 2.0, 1.0, help="Adjust the saturation of the image.")
        
        progress = st.progress(0)
        enhancer = ImageEnhance.Brightness(image)
        enhanced_image = enhancer.enhance(brightness)
        progress.progress(25)
        enhancer = ImageEnhance.Contrast(enhanced_image)
        enhanced_image = enhancer.enhance(contrast)
        progress.progress(50)
        enhancer = ImageEnhance.Color(enhanced_image)
        enhanced_image = enhancer.enhance(saturation)
        progress.progress(75)
        
        # Display images side by side
        col1, col2 = st.columns(2)
        with col1:
            st.image(image, caption='Uploaded Image', use_column_width=True)
        with col2:
            st.image(enhanced_image, caption='Enhanced Image', use_column_width=True)
        
        # Provide a download button
        buffer = BytesIO()
        enhanced_image.save(buffer, format="PNG")
        buffer.seek(0)
        st.download_button(
            label="Download Enhanced Image",
            data=buffer,
            file_name="enhanced_image.png",
            mime="image/png",
            help="Click to download the enhanced image."
        )
        st.success("Image ready for download")
        progress.progress(100)

# Bulk Background Remover Page
elif menu == "Bulk Background Remover":
    st.header("Bulk Background Remover")
    
    # File uploader
    uploaded_files = st.file_uploader("Choose images...", type=["jpg", "jpeg", "png"], accept_multiple_files=True, help="Upload multiple image files to remove backgrounds.")
    
    if uploaded_files:
        progress = st.progress(0)
        total_files = len(uploaded_files)
        
        def process_image(uploaded_file):
            image = Image.open(uploaded_file).convert("RGBA")
            image = resize_image(image, target_width=512)
            removed_bg_image = remove(image)
            cleaned_image = clean_borders(removed_bg_image)
            buffer = BytesIO()
            cleaned_image.save(buffer, format="PNG")
            buffer.seek(0)
            return {
                "image": cleaned_image,
                "buffer": buffer,
                "file_name": f"removed_bg_{uploaded_file.name}"
            }
        
        # Use ThreadPoolExecutor to process images in parallel
        with ThreadPoolExecutor() as executor:
            results = list(executor.map(process_image, uploaded_files))
        
        # Display the results
        col1, col2, col3 = st.columns(3)
        for idx, result in enumerate(results):
            col = [col1, col2, col3][idx % 3]
            with col:
                st.image(result["image"], caption='Removed Background', use_column_width=True)
                st.download_button(
                    label="Download",
                    data=result["buffer"],
                    file_name=result["file_name"],
                    mime="image/png",
                    help="Click to download the image with removed background."
                )
            
            progress.progress(int(((idx + 1) / total_files) * 100))
        
        # Create a ZIP file containing all processed images
        zip_buffer = BytesIO()
        with zipfile.ZipFile(zip_buffer, "w") as zip_file:
            for result in results:
                zip_file.writestr(result["file_name"], result["buffer"].getvalue())
        
        zip_buffer.seek(0)
        
        # Provide a download button for the ZIP file
        st.download_button(
            label="Download All",
            data=zip_buffer,
            file_name="removed_background_images.zip",
            mime="application/zip",
            help="Click to download all images with removed backgrounds."
        )
        
        st.success("Background removal completed for all images.")

# Help Page
elif menu == "Help":
    st.header("Help")
    st.write("""
        **Image Manipulation Tool** allows you to perform various image manipulation tasks including resizing, converting, cropping, and enhancing images.
        
        **Features:**
        - **Resize Image:** Resize your images by specifying dimensions or percentage.
        - **Convert Image:** Convert your images to different formats.
        - **Crop Image:** Crop your images to custom dimensions.
        - **Enhance Image:** Adjust brightness, contrast, and saturation of your images.
        - **Bulk Background Remover:** Remove backgrounds from multiple images at once.
        
    
        **Made by [@Himanshi-M](https://github.com/Himanshi-M)**
    """)

# Run the app
if __name__ == "__main__":
    pass  # No need to call any Streamlit method here
