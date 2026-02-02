
# Waste Classification Model Comparison Report

**Generated:** 2026-02-02 16:48:26

**Project:** MMU TCV6313 Waste Classification (Plastic, Aluminum, Paper)

---

## 1. Executive Summary

This report presents a comprehensive comparison of three deep learning models for waste classification:
- **EfficientNetB2** (TensorFlow)
- **ConvNeXt-Tiny** (PyTorch)
- **ViT-B16** (PyTorch)

Each model was evaluated on two datasets:
- **Preprocessed Dataset**: Offline preprocessed images
- **Raw Dataset**: Original unprocessed images

---

## 2. Best Overall Model

- **Model:** ConvNeXt-Tiny
- **Experiment:** Raw
- **Accuracy:** 0.7636
- **Precision:** 0.7719
- **Recall:** 0.7636
- **F1-Score:** 0.7647

---

## 3. Results Summary

| model_name        | experiment_type     |   accuracy |   precision |   recall |     f1 |   loss | timestamp           |
|:------------------|:--------------------|-----------:|------------:|---------:|-------:|-------:|:--------------------|
| ConvNeXt-Tiny     | Preprocessed        |     0.6548 |      0.653  |   0.6548 | 0.6523 | 1.4358 | 2026-02-02 4:48     |
| ConvNeXt-Tiny     | Preprocessed_on_Raw |     0.6735 |      0.7042 |   0.6735 | 0.6736 | 1.4087 | 2026-02-02 15:03:00 |
| ConvNeXt-Tiny     | Raw                 |     0.7636 |      0.7719 |   0.7636 | 0.7647 | 0.7135 | 2026-02-02 5:21     |
| CustomVGG_CNN     | Preprocessed        |     0.4259 |      0.4417 |   0.3696 | 0.4025 | 1.5325 | 2026-02-02 05:52:35 |
| CustomVGG_CNN     | Preprocessed_on_Raw |     0.272  |      0.2741 |   0.2345 | 0.2528 | 1.7704 | 2026-02-02 06:30:59 |
| CustomVGG_CNN     | Raw                 |     0.409  |      0.454  |   0.2964 | 0.3587 | 1.4145 | 2026-02-02 15:57:47 |
| EfficientNetB2    | Preprocessed        |     0.576  |      0.5918 |   0.576  | 0.5764 | 1.4235 | 2026-02-02 4:22     |
| EfficientNetB2    | Preprocessed_on_Raw |     0.7073 |      0.7357 |   0.7073 | 0.7094 | 1.0835 | 2026-02-02 5:08     |
| EfficientNetB2    | Raw                 |     0.7167 |      0.7198 |   0.7167 | 0.7167 | 0.8575 | 2026-02-02 5:04     |
| MobileNetV3-Large | Preprocessed        |     0.6398 |      0.6518 |   0.6323 | 0.6419 | 1.2183 | 2026-02-02 07:12:27 |
| MobileNetV3-Large | Preprocessed_on_Raw |     0.7111 |      0.7143 |   0.7036 | 0.7089 | 1.1396 | 2026-02-02 07:13:01 |
| MobileNetV3-Large | Raw                 |     0.7223 |      0.7297 |   0.7092 | 0.7193 | 0.9189 | 2026-02-02 16:06:09 |
| Resnet18          | Preprocessed        |     0.5497 |      0.5529 |   0.5478 | 0.5347 | 1.3516 | 2026-02-02 04:24:02 |
| Resnet18          | Preprocessed_on_Raw |     0.636  |      0.6356 |   0.636  | 0.626  | 1.2693 | 2026-02-02 04:34:15 |
| Resnet18          | Raw                 |     0.651  |      0.6573 |   0.651  | 0.6455 | 1.1046 | 2026-02-02 04:46:04 |
| Resnet50          | Preprocessed        |     0.2946 |      0.3189 |   0.2946 | 0.2848 | 1.102  | 2026-02-02 03:24:02 |
| Resnet50          | Preprocessed_on_Raw |     0.257  |      0.2529 |   0.257  | 0.24   | 1.1047 | 2026-02-02 03:34:15 |
| Resnet50          | Raw                 |     0.7335 |      0.7491 |   0.7335 | 0.7362 | 0.8459 | 2026-02-02 03:46:04 |
| ViT-B16           | Preprocessed        |     0.5985 |      0.597  |   0.5985 | 0.5975 | 1.9326 | 2026-02-02 06:24:02 |
| ViT-B16           | Preprocessed_on_Raw |     0.6492 |      0.6464 |   0.6492 | 0.6468 | 1.7289 | 2026-02-02 15:34:15 |
| ViT-B16           | Raw                 |     0.7242 |      0.7218 |   0.7242 | 0.7219 | 1.1055 | 2026-02-02 08:46:04 |

---

## 4. Key Findings

### Preprocessed vs Raw Dataset

**Resnet50:**
- Preprocessed: 0.2946
- Raw: 0.7335
- Improvement: -43.89%

**Resnet18:**
- Preprocessed: 0.5497
- Raw: 0.6510
- Improvement: -10.13%

**CustomVGG_CNN:**
- Preprocessed: 0.4259
- Raw: 0.4090
- Improvement: +1.69%

**ViT-B16:**
- Preprocessed: 0.5985
- Raw: 0.7242
- Improvement: -12.57%

**MobileNetV3-Large:**
- Preprocessed: 0.6398
- Raw: 0.7223
- Improvement: -8.25%

**ConvNeXt-Tiny:**
- Preprocessed: 0.6548
- Raw: 0.7636
- Improvement: -10.88%

**EfficientNetB2:**
- Preprocessed: 0.5760
- Raw: 0.7167
- Improvement: -14.07%


---

## 5. Recommendations

Based on the evaluation results:

1. **For Production Deployment:** Use the best overall model for optimal performance
2. **For Resource-Constrained Environments:** Consider the trade-off between accuracy and model size
3. **Data Preprocessing:** The results demonstrate the importance of proper preprocessing

---

## 6. Visualizations

See the following generated charts:
- `model_comparison.png` - Bar charts comparing all metrics
- `radar_comparison.png` - Radar charts for visual comparison
- `heatmap_comparison.png` - Heatmaps showing performance across all metrics

---

*Report generated automatically from training results*
