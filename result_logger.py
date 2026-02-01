import os
import csv
from datetime import datetime

def log_result(model_name, experiment_type, accuracy, precision, recall, f1, 
               loss=None, additional_info=None):
    """
    Log experiment results to final_results.csv
    
    Args:
        model_name (str): Name of the model (e.g., 'EfficientNetB2', 'ConvNeXt-Tiny', 'ViT-B16')
        experiment_type (str): Type of experiment (e.g., 'Preprocessed', 'Raw')
        accuracy (float): Test accuracy
        precision (float): Average precision
        recall (float): Average recall
        f1 (float): Average F1-score
        loss (float, optional): Test loss
        additional_info (str, optional): Any additional information
    """
    
    results_file = 'final_results.csv'
    file_exists = os.path.isfile(results_file)
    
    # Create or append to CSV
    with open(results_file, 'a', newline='') as f:
        fieldnames = ['timestamp', 'model_name', 'experiment_type', 
                     'accuracy', 'precision', 'recall', 'f1', 'loss', 'additional_info']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        
        # Write header if file doesn't exist
        if not file_exists:
            writer.writeheader()
        
        # Write result row
        writer.writerow({
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'model_name': model_name,
            'experiment_type': experiment_type,
            'accuracy': f'{accuracy:.4f}',
            'precision': f'{precision:.4f}',
            'recall': f'{recall:.4f}',
            'f1': f'{f1:.4f}',
            'loss': f'{loss:.4f}' if loss is not None else 'N/A',
            'additional_info': additional_info or 'N/A'
        })
    
    print(f"✓ Results logged: {model_name} - {experiment_type}")
    print(f"  Accuracy: {accuracy:.4f}, Precision: {precision:.4f}, Recall: {recall:.4f}, F1: {f1:.4f}")