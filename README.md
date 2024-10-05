# Image Manipulation Tool

This Python-based Image tool, built using **Streamlit**, allows users to perform various image manipulation tasks such as resizing, cropping, format conversion, and enhancement. With an intuitive, web-based interface, users can make adjustments with real-time previews. This tool is designed for single-image processing, providing a simple yet powerful platform for common image editing tasks.

**Approach:**
- The project started with research into image manipulation using Python libraries like `Pillow` and `Streamlit`. 
- Tools like `streamlit-cropper` were integrated for easier cropping.
  
**Additional Resources:**
- Streamlit documentation https://streamlit.io/
- Pillow library documentation https://readthedocs.org/projects/pillow/

## EXPLANATION

### DETAILS OF THE DIFFERENT FEATURES
1. **Image Resizing**: Users can resize images by height, width, or percentage.
2. **Image Cropping**: Provides an interactive cropping tool using `streamlit-cropper` with aspect ratio control.
3. **Format Conversion**: Converts images to popular formats like JPEG, PNG, BMP, and GIF.
4. **Enhancement**: Adjust brightness, contrast, sharpness, and color.

### WHAT I HAVE DONE
1. Researched tools like `Streamlit` and `Pillow` for image manipulation.
2. Developed a basic interface using `Streamlit` for uploading and previewing images.
3. Integrated resizing functionality with live previews.
4. Added image cropping using `streamlit-cropper`.
5. Implemented format conversion with compression quality controls.
6. Enabled image enhancement options (brightness, contrast, sharpness, color).
7. Ensured images can be saved and downloaded after edits.

### PROJECT TRADE-OFFS AND SOLUTIONS
1. **Trade-off 1**: Keeping the interface simple vs. adding advanced features.  
   - **Solution**: Prioritized simplicity, only adding essential features like resizing, cropping, and enhancement.
2. **Trade-off 2**: Balancing performance with real-time previews.  
   - **Solution**: Implemented lightweight image previews using `Pillow` and optimized backend logic.

### LIBRARIES NEEDED
- `streamlit`
- `Pillow`
- `streamlit-cropper`

### SCREENSHOTS
![image](https://github.com/user-attachments/assets/3900c172-722d-417a-ab00-b99d9cb32569)
![Screenshot_5-10-2024_172211_localhost](https://github.com/user-attachments/assets/bbafb96d-8418-4455-985c-c8fbcc371896)
![image](https://github.com/user-attachments/assets/6d06c6f7-06b0-4804-a686-f703ac85600f)
![image](https://github.com/user-attachments/assets/92d18dad-f108-420e-93f2-cfebd30fb171)
![image](https://github.com/user-attachments/assets/04589bab-1172-4333-b21d-5f588138bbad)
![image](https://github.com/user-attachments/assets/d4f2f013-9886-4e3f-a77b-8f25b458b3cb)


## CONCLUSION

### WHAT YOU HAVE LEARNED
- Practical application of Python in image processing.
- Using `Streamlit` to create web-based applications.
- Using `Pillow`'s `Image` to modify and handle images.
- Importance of balancing simplicity with functionality in a user interface.

### USE CASES OF THIS MODEL
1. **Content Creators**: Resize and enhance images for social media or blogs.
2. **Web Developers**: Optimize image sizes for website performance.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Himanshi-m/Image-Tool.git
   cd Image-Tool
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install Dependencies:**
   Install the required dependencies using the provided `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application:**
   Once dependencies are installed, run the tool with:
   ```bash
   streamlit run Image_Tool.py
   ```

### YOUR NAME
*Himanshi Maheshwari*

[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/himanshimaheshwari)
[![GitHub](https://img.shields.io/badge/github-%2312100E.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Himanshi-M)
[![Discord](https://img.shields.io/badge/discord-%237289DA.svg?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com/users/himanshi-maheshwari)

#### Happy Coding 🧑‍💻
### Show some &nbsp;❤️&nbsp; by &nbsp;🌟&nbsp; this repository!
