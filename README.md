# ROS Navigation Assignment

## 📌 Overview

This project implements a complete **ROS2 Navigation (Nav2) pipeline** for a mobile robot, including:

* Map loading
* Localization using AMCL
* Autonomous navigation using Nav2

The robot is capable of navigating to a given goal using a pre-built map while avoiding obstacles using sensor data.

---

## 🧱 System Architecture

The navigation pipeline consists of three main stages:

### 1. Map Server

* Loads a static map from a `.yaml` file
* Publishes the map on `/map` topic
* Managed using a lifecycle node

### 2. Localization (AMCL)

* Uses laser scan data (`/scan`) and map
* Estimates robot pose in the `map` frame
* Publishes transform: `map → odom`

### 3. Navigation (Nav2)

* Global planner generates path
* Local planner (DWB) controls motion
* Costmaps handle obstacle avoidance

---

## ⚙️ Setup & Build

```bash
cd ~/assignment_ws
colcon build
source install/setup.bash
```

---

## ▶️ How to Run

### Step 1: Load Map

```bash
ros2 launch testbed_navigation map_loader.launch.py
```

👉 Expected:

* `/map` topic is published
* Map visible in RViz (after adding Map display)

---

### Step 2: Start Localization

```bash
ros2 launch testbed_localization localization.launch.py
```

👉 In RViz:

* Set **Fixed Frame = map**
* Use **"2D Pose Estimate"** to initialize robot pose
* Robot should align with map

---

### Step 3: Start Navigation

```bash
ros2 launch testbed_navigation navigation.launch.py
```

👉 In RViz:

* Use **"Nav2 Goal"** to send goal
* Robot should plan and move autonomously

---

## 🧠 Key Concepts Used

* TF Tree: `map → odom → base_link`
* Costmaps (local + global)
* DWB Local Planner
* AMCL Particle Filter
* Lifecycle Nodes

---

## ⚠️ Challenges Faced & Fixes

### 1. TF Extrapolation Error

**Issue:**

```
Lookup would require extrapolation into the past
```

**Fix:**

* Adjusted `transform_tolerance`
* Ensured proper time synchronization

---

### 2. Robot Oscillation Near Walls

**Issue:**

* Robot rotates continuously near obstacles
* Fails to find valid trajectory

**Fixes:**

* Reduced inflation radius
* Adjusted robot footprint
* Allowed backward motion (`min_vel_x < 0`)
* Tuned DWB parameters

---

### 3. No Valid Trajectories

**Issue:**

```
No valid trajectories out of N
```

**Fix:**

* Increased trajectory sampling
* Relaxed costmap constraints

---

### 4. Goal Failure Near Target

**Issue:**

* Robot reaches near goal but fails

**Fix:**

* Tuned goal tolerances
* Adjusted controller parameters

---

### 5. Map Not Visible Initially

**Issue:**

* Map not appearing in RViz

**Fix:**

* Added Map display manually
* Set correct Fixed Frame (`map`)

---

## 🔧 Important Parameters

### Navigation Tuning Highlights

```yaml
FollowPath:
  max_vel_x: 0.35
  min_vel_x: -0.2
  max_vel_theta: 1.0

inflation_layer:
  inflation_radius: 0.2

local_costmap:
  width: 8.0
  height: 8.0
```

---

## 🎯 Expected Behavior

* Robot localizes correctly on map
* Smooth path planning
* Avoids obstacles
* Reaches goal without oscillation

---

## 🚀 Future Improvements

* Add SLAM instead of static map
* Improve dynamic obstacle handling
* Integrate with real robot hardware
* Use advanced planners (TEB / MPC)

---

## 👨‍💻 Author

Kuldip Birhade
Mechanical Engineering | Robotics Enthusiast

---
