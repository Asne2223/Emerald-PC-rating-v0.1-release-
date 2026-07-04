import streamlit as st
import sys
import io

# Set up the web page title and icon
st.set_page_config(page_title="Emerald PC Rating Tool", page_icon="✳️")
st.title("✳️ Emerald PC Rating Tool")
st.write("Welcome! Enter your system specifications below to check your hardware rating.")

# ==========================================
# 1. YOUR WEB INPUTS
# ==========================================
# This replaces terminal input() with beautiful web text boxes
cpu_input = st.text_input("🖥️ Enter CPU Name (e.g., Core i7-13700K):")
gpu_input = st.text_input("🎮 Enter GPU Name (e.g., RTX 4090):")
ram_input = st.number_input("💾 Enter RAM Size (GB):", min_value=1, value=16)

# ==========================================
# 2. RUN BUTTON
# ==========================================
if st.button("🚀 Rate My PC"):
    
    # This clever trick intercepts your original print() statements 
    # so they show up directly on the web page instead of hiding in the terminal!
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    
    try:
        # ==========================================
        # 3. PASTE YOUR EXACT LOGIC BELOW THIS LINE
        # ==========================================
        # (Keep all your original variables, conditions, and print statements here)
        
        # --- EXAMPLE OF YOUR UNTOUCHED LOGIC ---
        print("Initializing Emerald Rating System...")
        print(f"Checking CPU: {cpu_input}")
        print(f"Checking GPU: {gpu_input}")
        print(f"Checking RAM: {ram_input} GB")
        
        # Put your exact dbgpu lookups, calculations, and math loops here:
        if ram_input >= 16:
            print("RAM Status: EXCELLENT (Meets high-end ratings)")
        else:
            print("RAM Status: WARNING (Upgrade recommended for modern games)")
            
        print("Analysis complete! Thank you for using Emerald PC Rating Tool.")
        # ==========================================
        # PASTE YOUR EXACT LOGIC ABOVE THIS LINE
        # ==========================================
        
        # Display all your original prints onto the web dashboard screen
        printed_output = sys.stdout.getvalue()
        st.subheader("📋 System Rating Results")
        st.code(printed_output, language="text")
        
    except Exception as e:
        st.error(f"An error occurred during calculations: {e}")
        
    finally:
        # Reset the print system back to normal
        sys.stdout = old_stdout

