import streamlit as st
import time

# -------------------------
# 2D SHAPES
# -------------------------

def triangle_perimeter(a, b, c):
    return a + b + c

def triangle_area(a, b, c):
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

def square_perimeter(side):
    return 4 * side

def square_area(side):
    return side ** 2

def rectangle_perimeter(l, b):
    return 2 * (l + b)

def area_rectangle(l, b):
    return l * b

def circle_perimeter(r):
    return 2 * (22 / 7) * r

def area_circle(r):
    return (22 / 7) * (r ** 2)

# -------------------------
# 3D OBJECTS
# -------------------------

def cone_tsa(r, l):
    return (22 / 7) * r * (r + l)

def cone_vol(r, h):
    return (1 / 3) * (22 / 7) * (r ** 2) * h

def cube_tsa(s):
    return 6 * (s ** 2)

def cube_vol(s):
    return s ** 3

def cuboid_tsa(l, b, h):
    return 2 * (l * b + b * h + h * l)

def cuboid_vol(l, b, h):
    return l * b * h

def sphere_tsa(r):
    return 4 * (22 / 7) * (r ** 2)

def sphere_vol(r):
    return (4 / 3) * (22 / 7) * (r ** 3)

def cylinder_tsa(r, h):
    return 2 * (22 / 7) * r * (h + r)

def cylinder_vol(r, h):
    return (22 / 7) * (r ** 2) * h

# -------------------------
# STREAMLIT APP
# -------------------------

st.title("Geometry Calculator")

# Triangle
st.header("2D Shapes")
st.subheader("Triangle")

a = st.number_input("Side 1", min_value=0.0, key="tri_a")
b = st.number_input("Side 2", min_value=0.0, key="tri_b")
c = st.number_input("Side 3", min_value=0.0, key="tri_c")

col1, col2 = st.columns(2)

with col1:
    st.metric("Perimeter", round(triangle_perimeter(a, b, c), 2))

with col2:
    if a + b > c and a + c > b and b + c > a:
        st.metric("Area", round(triangle_area(a, b, c), 2))
    else:
        st.metric("Area", "Invalid")

st.divider()

# Square
st.subheader("Square")

s = st.number_input("Square Side", min_value=0.0, key="sq_s")

col1, col2 = st.columns(2)

with col1:
    st.metric("Perimeter", round(square_perimeter(s), 2))

with col2:
    st.metric("Area", round(square_area(s), 2))

st.divider()

# Rectangle
st.subheader("Rectangle")

l = st.number_input("Length", min_value=0.0, key="rec_l")
b = st.number_input("Breadth", min_value=0.0, key="rec_b")

col1, col2 = st.columns(2)

with col1:
    st.metric("Perimeter", round(rectangle_perimeter(l, b), 2))

with col2:
    st.metric("Area", round(area_rectangle(l, b), 2))

st.divider()

# Circle
st.subheader("Circle")

r = st.number_input("Radius", min_value=0.0, key="cir_r")

col1, col2 = st.columns(2)

with col1:
    st.metric("Circumference", round(circle_perimeter(r), 2))

with col2:
    st.metric("Area", round(area_circle(r), 2))

st.divider()

# -------------------------
# 3D OBJECTS
# -------------------------

st.header("3D Objects")

# Cone
st.subheader("Cone")

r_cone = st.number_input("Cone Radius", min_value=0.0, key="cone_r")
l_cone = st.number_input("Cone Slant Height", min_value=0.0, key="cone_l")
h_cone = st.number_input("Cone Height", min_value=0.0, key="cone_h")

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Surface Area", round(cone_tsa(r_cone, l_cone), 2))

with col2:
    st.metric("Volume", round(cone_vol(r_cone, h_cone), 2))

st.divider()

# Cube
st.subheader("Cube")

s_cube = st.number_input("Cube Side", min_value=0.0, key="cube_s")

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Surface Area", round(cube_tsa(s_cube), 2))

with col2:
    st.metric("Volume", round(cube_vol(s_cube), 2))

st.divider()

# Cuboid
st.subheader("Cuboid")

l_cub = st.number_input("Cuboid Length", min_value=0.0, key="cub_l")
b_cub = st.number_input("Cuboid Breadth", min_value=0.0, key="cub_b")
h_cub = st.number_input("Cuboid Height", min_value=0.0, key="cub_h")

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Surface Area", round(cuboid_tsa(l_cub, b_cub, h_cub), 2))

with col2:
    st.metric("Volume", round(cuboid_vol(l_cub, b_cub, h_cub), 2))

st.divider()

# Sphere
st.subheader("Sphere")

r_sphere = st.number_input("Sphere Radius", min_value=0.0, key="sphere_r")

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Surface Area", round(sphere_tsa(r_sphere), 2))

with col2:
    st.metric("Volume", round(sphere_vol(r_sphere), 2))

st.divider()

# Cylinder
st.subheader("Cylinder")

r_cyl = st.number_input("Cylinder Radius", min_value=0.0, key="cyl_r")
h_cyl = st.number_input("Cylinder Height", min_value=0.0, key="cyl_h")

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Surface Area", round(cylinder_tsa(r_cyl, h_cyl), 2))

with col2:
    st.metric("Volume", round(cylinder_vol(r_cyl, h_cyl), 2))

st.divider()

st.success("Geometry Calculator Loaded Successfully!")
