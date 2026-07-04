import streamlit as st
import sys
import io
from dbgpu import GPUDatabase

st.set_page_config(page_title="Emerald PC Rating Tool", page_icon="✳️")
st.title("✳️ Emerald PC Rating Tool")
st.write("Welcome to the PC rating program!")

db = GPUDatabase.default()

# ==========================================
# 1. VISUAL SIDEBAR SELECTION PANEL
# ==========================================
st.sidebar.header("⚙️ Configure Specs")
RAM = st.sidebar.number_input("How much RAM does your PC have? (GB)", min_value=1, value=16)

proceed_gpu = st.sidebar.checkbox("Proceed to GPU rating?", value=True)
gpu_name = ""
use_db = "no"
GHz = 0.0

if proceed_gpu:
    use_db_toggle = st.sidebar.toggle("Use GPU Database Lookup", value=True)
    if use_db_toggle:
        use_db = "yes"
        gpu_name = st.sidebar.text_input("GPU Model:", value="GTX 1080")
    else:
        use_db = "no"
        GHz = st.sidebar.number_input("DIY GPU speed (GHz):", min_value=0.0, max_value=10.0, value=1.8, step=0.1)

proceed_cpu = st.sidebar.checkbox("Proceed to CPU rating?", value=True)
cpu_GHz = 0.0
if proceed_cpu:
    cpu_GHz = st.sidebar.number_input("How many GHz is your CPU?", min_value=0.0, max_value=10.0, value=3.2, step=0.1)

# ==========================================
# 2. RUN SYSTEM CHECK
# ==========================================
if st.button("🚀 Run Hardware Rating"):
    
    # Intercept print commands to feed the visual dashboard box
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    
    try:
        # ==========================================
        # 3. MUTER PROCESS FOR INTERACTIVE PROMPTS
        # ==========================================
        print("Welcome to PC rating programm!")
        print(f"Analyzing Configuration... [RAM: {RAM}GB]")
        
        if RAM < 6:
            print("Your PC is a bit low on RAM...")
        else:
            print("Your pc has a good amount of RAM!")
            
        print("RAM check done!")
        
        if proceed_gpu:
            print("[System Log]: Accessing Graphic Processing Unit metrics...")
            
            if use_db == "yes":
                print(f"Searching database parameters for: '{gpu_name}'")
                
                match = db.search(gpu_name)
                if match:
                    print("Found in database:", match.name)
                    print("VRAM Size in GB:", match.memory_size_gb)
                    GHz_calc = match.boost_clock_mhz / 1000
                    print("Your GPU clock works at", GHz_calc, "GHz")
                else:
                    print(f"GPU query '{gpu_name}' not found in database records.")
                    
            else:
                print(f"Evaluating user hardware parameter profile... [Clock Speed: {GHz} GHz]")
                if GHz < 2.0:
                    print("Your GPU is not that great...")
                else:
                    print("Wow! Your PC has a great GPU!")
        else:
            print("GPU Diagnostics bypassed by user config selection.")

        if proceed_cpu:
            print(f"Evaluating Central Processing Unit metrics... [Clock Speed: {cpu_GHz} GHz]")
            if cpu_GHz < 3.0:
                print("Your CPU is decent - bad...")
            else:
                print("Your CPU is great!")
        else:
            print("CPU Diagnostics bypassed by user config selection.")
            
        # Push the print pipeline output data live onto the web page container
        printed_output = sys.stdout.getvalue()
        st.subheader("📋 System Diagnosis Logs")
        st.code(printed_output, language="text")
        
    except Exception as e:
        st.error(f"An execution thread runtime error occurred: {e}")
        
    finally:
        sys.stdout = old_stdout
