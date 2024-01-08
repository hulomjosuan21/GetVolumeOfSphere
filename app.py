import streamlit as st
import math
st.set_page_config("Get Volume of Sphere", layout='centered', page_icon='📖',initial_sidebar_state='auto')
def getVolumeOfSphere(r, d):
    Pi = 3.14159
    V = 0.0
    x = 0
    if r != 0 and d != 0:
        d = 0

    if r != 0:
        x = r
        r = int(math.pow(r, 3))
        V = 4 * r
        V = V / 3
        V = V * Pi
    elif d != 0:
        r = d // 2
        x = r
        r = int(math.pow(r, 3))
        V = 4 * r
        V = V / 3
        V = V * Pi
    else:
        V = 0

    return [x,V]

def main():
    
    r = st.number_input("Radius: ")
    d = st.number_input("Diameter: ")
    
    v = getVolumeOfSphere(r,d)
    
    if st.button("Calculate Volume of sphere"):
        st.write(f"Volume of sphere with radius of {v[0]} is {v[1]:.2f}")
    st.write("Copyright © 2024 Josuan. All rights reserved.")
if __name__ == '__main__':
    main()