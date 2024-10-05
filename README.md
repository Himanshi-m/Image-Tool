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
![image](https://github.com/user-attachments/assets/c44b1640-ab7d-4915-9c58-8149a209db24)
![image](https://github.com/user-attachments/assets/447f928c-c2be-4951-b879-42514f7b761e)
![image](https://github.com/user-attachments/assets/9ae6f7e6-6643-43cb-b324-c41592b10566)
![image](https://github.com/user-attachments/assets/a8982ded-ed98-4b18-b23b-9f3a44307f97)
![image](https://github.com/user-attachments/assets/d981d58c-f040-4934-8e97-7e2eb5f59e88)
![image](https://github.com/user-attachments/assets/559dd9bc-8e94-48ef-a138-91a17cf45003)


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
