# 🛒 Supermarket Sales Data Cleaning

## 📌 Overview

This project focuses on **cleaning and preprocessing supermarket sales data** to prepare it for analysis and visualization. Using **Pandas**, missing values were handled, columns standardized, and unnecessary data removed.

---

## 🧹 Key Steps

* Loaded dataset (`supermarket_sales_with_nulls.xlsx`).
* Explored data (shape, info, stats, missing values).
* Standardized column names.
* Dropped `unitprice` column.
* Filled missing values:

  * `city` & `payment` → mode
  * `quantity` → median
* Converted `time` to datetime.
* Verified dataset is clean.

---

## 🛠 Tools

* Python
* Pandas

---

## 🚀 Run the Project

```bash
pip install pandas
python supermarket_sales_cleaning.py
```

---

## ✅ Output

* Cleaned dataset with no missing values.
* Consistent column names and correct data types.
* Ready for visualization and reporting.

