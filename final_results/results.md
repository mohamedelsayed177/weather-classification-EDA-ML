# Weather Classification Model Results (Summary)

| Model                  | Accuracy | Precision | Recall | F1 Score |
|------------------------|---------|-----------|--------|----------|
| Logistic Regression    | 0.854   | 0.854     | 0.854  | 0.854    |
| Support Vector Machine | 0.907   | 0.910     | 0.907  | 0.908    |
| Random Forest          | 0.916   | 0.917     | 0.916  | 0.916    |

## Per-Class Metrics

### Logistic Regression
- Class 0 (Cloudy): Precision 0.81 | Recall 0.83 | F1 0.82  
- Class 1 (Rainy): Precision 0.84 | Recall 0.86 | F1 0.85  
- Class 2 (Snowy): Precision 0.90 | Recall 0.91 | F1 0.91  
- Class 3 (Sunny): Precision 0.87 | Recall 0.81 | F1 0.84  

### Support Vector Machine
- Class 0 (Cloudy): Precision 0.83 | Recall 0.91 | F1 0.87  
- Class 1 (Rainy): Precision 0.91 | Recall 0.91 | F1 0.91  
- Class 2 (Snowy): Precision 0.96 | Recall 0.91 | F1 0.93  
- Class 3 (Sunny): Precision 0.94 | Recall 0.90 | F1 0.92  

### Random Forest
- Class 0 (Cloudy): Precision 0.87 | Recall 0.92 | F1 0.89  
- Class 1 (Rainy): Precision 0.90 | Recall 0.91 | F1 0.91  
- Class 2 (Snowy): Precision 0.96 | Recall 0.91 | F1 0.93  
- Class 3 (Sunny): Precision 0.94 | Recall 0.92 | F1 0.93  

## Conclusion
- **Random Forest** achieved the best overall performance.  
- **SVM** performs well, especially in precision.  
- **Logistic Regression** is the baseline model with decent accuracy (~85%).
