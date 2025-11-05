# **Weather Classification Model Results (Summary)**

| Model                  | Accuracy | Precision | Recall  | F1 Score |
|------------------------|-----------|-----------|----------|----------|
| Logistic Regression    | 0.8538    | 0.8544    | 0.8538   | 0.8537   |
| Support Vector Machine | 0.9072    | 0.9101    | 0.9072   | 0.9079   |
| Random Forest          | 0.9155    | 0.9169    | 0.9155   | 0.9159   |

---

## **Per-Class Metrics**

### **Logistic Regression**
- **Class 0 (Cloudy):** Precision 0.81 | Recall 0.83 | F1 0.82  
- **Class 1 (Rainy):** Precision 0.84 | Recall 0.86 | F1 0.85  
- **Class 2 (Snowy):** Precision 0.90 | Recall 0.91 | F1 0.91  
- **Class 3 (Sunny):** Precision 0.87 | Recall 0.81 | F1 0.84  

---

### **Support Vector Machine**
- **Class 0 (Cloudy):** Precision 0.83 | Recall 0.91 | F1 0.87  
- **Class 1 (Rainy):** Precision 0.91 | Recall 0.91 | F1 0.91  
- **Class 2 (Snowy):** Precision 0.96 | Recall 0.91 | F1 0.93  
- **Class 3 (Sunny):** Precision 0.94 | Recall 0.90 | F1 0.92  

---

### **Random Forest**
- **Class 0 (Cloudy):** Precision 0.87 | Recall 0.92 | F1 0.89  
- **Class 1 (Rainy):** Precision 0.90 | Recall 0.91 | F1 0.91  
- **Class 2 (Snowy):** Precision 0.96 | Recall 0.91 | F1 0.93  
- **Class 3 (Sunny):** Precision 0.94 | Recall 0.92 | F1 0.93  

---

## **Conclusion**
- **Random Forest** achieved the **best overall performance** across all metrics (Accuracy ≈ 91.6%).  
- **SVM** performed very well, especially in **precision and balance** between classes.  
- **Logistic Regression** served as a solid **baseline model** with consistent accuracy (~85%).  
