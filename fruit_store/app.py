import streamlit as st
from crud import create_fruit, read_fruits, update_fruit, delete_fruit
from models import Fruta

# Streamlit app
st.title("Tienda de Frutas")

# Create
st.header("Agregar nueva fruta")
name = st.text_input("Nombre de la fruta")
quantity = st.number_input("Cantidad", min_value=0)
price = st.number_input("Precio", min_value=0.0, format="%.2f")
family = st.text_input("Familia")
genus = st.text_input("Género")
order = st.text_input("Orden")
carbohydrates = st.number_input("Carbohidratos (g/100g)", min_value=0.0, format="%.2f")
protein = st.number_input("Proteínas (g/100g)", min_value=0.0, format="%.2f")
fat = st.number_input("Grasas (g/100g)", min_value=0.0, format="%.2f")
calories = st.number_input("Calorías (kcal/100g)", min_value=0.0, format="%.2f")
sugar = st.number_input("Azúcar (g/100g)", min_value=0.0, format="%.2f")

if st.button("Agregar"):
    new_fruit = Fruta(name=name, quantity=quantity, price=price, family=family, genus=genus, order=order, carbohydrates=carbohydrates, protein=protein, fat=fat, calories=calories, sugar=sugar)
    create_fruit(new_fruit)
    st.success(f"Fruta '{name}' agregada exitosamente!")

# Read
st.header("Lista de frutas")
fruits = read_fruits()
for fruit in fruits:
    st.write(f"ID: {fruit['id']}, Nombre: {fruit['name']}, Cantidad: {fruit['quantity']}, Precio: {fruit['price']}, Familia: {fruit['family']}, Género: {fruit['genus']}, Orden: {fruit['order']}, Carbohidratos: {fruit['carbohydrates']}g, Proteínas: {fruit['protein']}g, Grasas: {fruit['fat']}g, Calorías: {fruit['calories']}kcal, Azúcar: {fruit['sugar']}g")

# Update
st.header("Actualizar fruta")
update_id = st.number_input("ID de la fruta a actualizar", min_value=0)
new_name = st.text_input("Nuevo nombre de la fruta")
new_quantity = st.number_input("Nueva cantidad", min_value=0)
new_price = st.number_input("Nuevo precio", min_value=0.0, format="%.2f")
new_family = st.text_input("Nueva familia")
new_genus = st.text_input("Nuevo género")
new_order = st.text_input("Nuevo orden")
new_carbohydrates = st.number_input("Nuevos carbohidratos (g/100g)", min_value=0.0, format="%.2f")
new_protein = st.number_input("Nuevas proteínas (g/100g)", min_value=0.0, format="%.2f")
new_fat = st.number_input("Nuevas grasas (g/100g)", min_value=0.0, format="%.2f")
new_calories = st.number_input("Nuevas calorías (kcal/100g)", min_value=0.0, format="%.2f")
new_sugar = st.number_input("Nuevo azúcar (g/100g)", min_value=0.0, format="%.2f")

if st.button("Actualizar"):
    updated_fruit = Fruta(name=new_name, quantity=new_quantity, price=new_price, family=new_family, genus=new_genus, order=new_order, carbohydrates=new_carbohydrates, protein=new_protein, fat=new_fat, calories=new_calories, sugar=new_sugar)
    update_fruit(update_id, updated_fruit)
    st.success(f"Fruta con ID '{update_id}' actualizada exitosamente!")

# Delete
st.header("Eliminar fruta")
delete_id = st.number_input("ID de la fruta a eliminar", min_value=0)

if st.button("Eliminar"):
    delete_fruit(delete_id)
    st.success(f"Fruta con ID '{delete_id}' eliminada exitosamente!")
