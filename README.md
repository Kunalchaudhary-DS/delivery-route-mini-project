# 🚚 Delivery Route Optimization System

## 📌 Project Overview

This project simulates a real-world logistics problem where delivery routes are optimized using multiple algorithmic techniques. It integrates concepts from Design and Analysis of Algorithms (ADA) to efficiently handle delivery constraints such as distance, time, and vehicle capacity.

---

## 🎯 Objectives

* Minimize total delivery distance
* Maximize value of delivered parcels
* Satisfy delivery time constraints
* Efficiently utilize vehicle capacity

---

## 🧠 Algorithms Used

### 🔹 Greedy Algorithm

* Used for parcel selection
* Based on value-to-weight ratio
* Fast but not always globally optimal

---

### 🔹 Dynamic Programming (DP)

* Used for validating delivery time constraints
* Ensures deadlines are satisfied

---

### 🔹 Recursion

* Used for route cost calculation
* Demonstrates exponential complexity

---

### 🔹 Dijkstra’s Algorithm

* Computes shortest path from warehouse to all locations
* Efficient for routing decisions

---

### 🔹 Minimum Spanning Tree (MST)

* Connects all nodes with minimum total cost
* Useful for network optimization

---

### 🔹 Traveling Salesman Problem (TSP)

* Finds optimal delivery route
* Guarantees minimum total distance
* Computationally expensive

---

## 📊 Visualizations & Analysis

The project includes multiple visualizations:

* Graph representation of delivery network
* Algorithm time comparison
* DP vs Recursion comparison
* Dijkstra vs MST comparison
* TSP scalability analysis
* Profit vs weight analysis
* Route cost breakdown

---

## 📈 Key Insights

* Greedy is fastest but not always optimal
* TSP ensures optimal routing but has high complexity
* Recursion is not scalable for large inputs
* Dijkstra and MST solve different optimization problems
* Combining algorithms yields better results than using a single approach

---

## 🏗️ Project Structure

```
delivery-route-mini-project/
│
├── notebooks/
│   └── main.ipynb
│
├── src/
│   ├── graph_utils.py
│   ├── greedy.py
│   ├── tsp.py
│   ├── dp.py
│   └── recursion.py
│
├── images/
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

1. Clone the repository:

```
git clone <your-repo-link>
cd delivery-route-mini-project
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run Jupyter Notebook:

```
jupyter notebook
```

4. Open:

```
notebooks/main.ipynb
```

---

## ▶️ How It Works

1. Define graph and input data
2. Select parcels using Greedy
3. Compute optimal route using TSP
4. Validate constraints using DP
5. Analyze performance using graphs

---

## ⚠️ Limitations

* Works only for small datasets (TSP limitation)
* Single vehicle assumption
* Simplified time constraint handling

---

## 🚀 Future Improvements

* Multi-vehicle routing
* Real-time traffic integration
* Fuel cost optimization
* Scalable TSP approximations

---

## 👨‍💻 Author

Kunal

---

## ✅ Conclusion

This project demonstrates how multiple algorithmic strategies can be combined to solve complex logistics problems, highlighting trade-offs between efficiency, optimality, and scalability.
