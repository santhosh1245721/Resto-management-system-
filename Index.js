// index.js

const apiUrl = "http://localhost:5000";

// Function to get orders
async function getOrders() {
  const response = await fetch(`${apiUrl}/orders`);
  const orders = await response.json();
  console.log(orders);
  // Render orders in the UI
}

// Function to create order
async function createOrder(orderData) {
  const response = await fetch(`${apiUrl}/orders`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(orderData),
  });
  const result = await response.json();
  console.log(result);
  // Render success message in the UI
}

// Function to get menu
async function getMenu() {
  const response = await fetch(`${apiUrl}/menu`);
  const menu = await response.json();
  console.log(menu);
  // Render menu in the UI
}

// Function to create menu item
async function createMenuItem(menuItemData) {
  const response = await fetch(`${apiUrl}/menu`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(menuItemData),
  });
  const result = await response.json();
  console.log(result);
  // Render success message in the UI
}

// Function to get tables
async function getTables() {
  const response = await fetch(`${apiUrl}/tables`);
  const tables = await response.json();
  console.log(tables);
  // Render tables in the UI
}

// Function to create table
async function createTable(tableData) {
  const response = await fetch(`${apiUrl}/tables`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(tableData),
  });
  const result = await response.json();
  console.log(result);
  // Render success message in the UI
}

// Example usage
getOrders();
createOrder({ table_number: 1, order_items: ["Burger", "Fries"] });
getMenu();
createMenuItem({ name: "New Burger", price: 10.99 });
getTables();
createTable({ table_number: 5, capacity: 4 });
