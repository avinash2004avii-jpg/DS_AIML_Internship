import streamlit as st
from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image
import pandas as pd
import os

# Set page configuration with a premium look
st.set_page_config(
    page_title="YOLOv8 Object Detection Hub",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Premium CSS Styling for Sleek Appearance & Micro-animations
st.markdown("""
<style>
    /* Custom background & text colors */
    .stApp {
        background-color: #0f111a;
        color: #f0f2f6;
    }
    
    /* Title text styling */
    .main-title {
        font-family: 'Outfit', 'Inter', sans-serif;
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(135deg, #ff007f 0%, #7f00ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.5rem;
        animation: fadeIn 1.5s ease-in-out;
    }
    
    .subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 1.2rem;
        color: #94a3b8;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    /* Sleek card container */
    .stat-card {
        background: rgba(30, 41, 59, 0.4);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.2);
        backdrop-filter: blur(8px);
        margin-bottom: 1rem;
        transition: transform 0.3s ease, border-color 0.3s ease;
    }
    .stat-card:hover {
        transform: translateY(-4px);
        border-color: #7f00ff;
    }
    
    /* Fade-in animation */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
</style>
""", unsafe_allow_html=True)

# Application Header
st.markdown("<h1 class='main-title'>🎯 YOLOv8 Object Detection Hub</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Upload custom images, select modern YOLOv8 architectures, and adjust detection parameters in real time!</p>", unsafe_allow_html=True)

# Sidebar - Settings Configuration
st.sidebar.image("https://raw.githubusercontent.com/ultralytics/assets/main/logo/Logo-YOLOv8-Small.png", use_container_width=True)
st.sidebar.markdown("### ⚙️ Model Parameters")

# Model Selection
model_option = st.sidebar.selectbox(
    "Choose YOLOv8 Model Architecture",
    ["YOLOv8 Nano (Fastest)", "YOLOv8 Small (Balanced)", "YOLOv8 Medium (Accurate)", "YOLOv8 Large (Highly Accurate)"],
    index=0
)

# Map human-readable models to weights files
model_map = {
    "YOLOv8 Nano (Fastest)": "yolov8n.pt",
    "YOLOv8 Small (Balanced)": "yolov8s.pt",
    "YOLOv8 Medium (Accurate)": "yolov8m.pt",
    "YOLOv8 Large (Highly Accurate)": "yolov8l.pt"
}
model_file = model_map[model_option]

# Slider controls
conf_threshold = st.sidebar.slider("Confidence Threshold", min_value=0.0, max_value=1.0, value=0.25, step=0.05)
iou_threshold = st.sidebar.slider("IoU Threshold", min_value=0.0, max_value=1.0, value=0.45, step=0.05)

# Load the selected model
@st.cache_resource
def load_yolo_model(model_name):
    return YOLO(model_name)

try:
    with st.spinner(f"Loading {model_option}... Please wait."):
        model = load_yolo_model(model_file)
    st.sidebar.success(f"Loaded {model_file} successfully!")
except Exception as e:
    st.sidebar.error(f"Error loading model: {e}")

# Main Layout
tab1, tab2 = st.tabs(["🖼️ Image Detection", "ℹ️ About YOLOv8"])

with tab1:
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("<div class='stat-card'><h3>📥 Input Source</h3>", unsafe_allow_html=True)
        source_type = st.radio("Choose Input Image", ["Sample Image (traffic.jpg)", "Upload Custom Image"])
        
        uploaded_file = None
        input_image = None
        
        if source_type == "Sample Image (traffic.jpg)":
            if os.path.exists("traffic.jpg"):
                input_image = Image.open("traffic.jpg")
            else:
                st.error("Sample image `traffic.jpg` not found in current directory.")
        else:
            uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])
            if uploaded_file is not None:
                input_image = Image.open(uploaded_file)
        
        if input_image is not None:
            st.image(input_image, caption="Source Image", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
    with col2:
        st.markdown("<div class='stat-card'><h3>⚡ Detection Output</h3>", unsafe_allow_html=True)
        
        if input_image is not None:
            # Run detection button
            if st.button("🚀 Run YOLOv8 Object Detection", use_container_width=True):
                # Convert PIL image to OpenCV format
                img_array = np.array(input_image)
                # Convert RGB to BGR for OpenCV
                img_bgr = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
                
                # Perform inference
                with st.spinner("Processing image..."):
                    results = model(img_bgr, conf=conf_threshold, iou=iou_threshold)
                
                # Plot annotated boxes on the BGR image
                annotated_img_bgr = results[0].plot()
                # Convert BGR back to RGB for display
                annotated_img_rgb = cv2.cvtColor(annotated_img_bgr, cv2.COLOR_BGR2RGB)
                
                # Show results
                st.image(annotated_img_rgb, caption="YOLOv8 Detection Output", use_container_width=True)
                
                # Download button
                result_pil = Image.fromarray(annotated_img_rgb)
                # Save to byte array for download
                from io import BytesIO
                buf = BytesIO()
                result_pil.save(buf, format="JPEG")
                byte_im = buf.getvalue()
                st.download_button(
                    label="📥 Download Annotated Image",
                    data=byte_im,
                    file_name="yolov8_output.jpg",
                    mime="image/jpeg",
                    use_container_width=True
                )
                
                # Analysis of detected objects
                boxes = results[0].boxes
                if len(boxes) > 0:
                    class_ids = boxes.cls.cpu().numpy().astype(int)
                    class_names = [model.names[cid] for cid in class_ids]
                    
                    # Compute counts
                    unique, counts = np.unique(class_names, return_counts=True)
                    df_counts = pd.DataFrame({'Detected Object': unique, 'Count': counts}).sort_values(by='Count', ascending=False)
                    
                    st.markdown("#### 📊 Object Analysis Breakdown")
                    st.dataframe(df_counts, use_container_width=True, hide_index=True)
                else:
                    st.info("No objects detected above the confidence threshold.")
            else:
                st.info("Click the button above to run the YOLOv8 object detector.")
        else:
            st.warning("Please upload an image or choose the sample to start.")
        st.markdown("</div>", unsafe_allow_html=True)

with tab2:
    st.markdown("""
    ### 🚀 Deep Dive: What is YOLOv8?
    **YOLOv8** (You Only Look Once Version 8) is the state-of-the-art model developed by **Ultralytics**.
    
    #### Key Features:
    * **Extremely Fast:** Optimized for real-time inference on edge devices, CPU, and GPU.
    * **Unified Framework:** One architecture for Object Detection, Instance Segmentation, Image Classification, Pose Estimation, and Object Tracking.
    * **New Anchor-Free Architecture:** Predicts directly the center of an object instead of the offset from a known anchor box.
    
    #### Model Variants:
    1. **Nano (`yolov8n.pt`):** Best for CPU and mobile devices. Ultralightweight.
    2. **Small (`yolov8s.pt`):** Great compromise between speed and accuracy.
    3. **Medium (`yolov8m.pt`):** Ideal for general real-time use with high accuracy.
    4. **Large (`yolov8l.pt`):** High precision, best suited for robust server deployment.
    """)
