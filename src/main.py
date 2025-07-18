from data_generation.generator import DataGenerator
from data_masking.masker import DataMasker
from data_management.manager import DataManager

def main():
    # Initialize the data generator
    data_generator = DataGenerator()
    
    # Generate test data (lista de usuários)
    test_data = data_generator.generate_data("user", count=10)

    # Initialize the data masker
    data_masker = DataMasker()
    
    # Mask sensitive information in all test data
    masked_data = [data_masker.mask_data(user) for user in test_data]

    # Initialize the data manager
    data_manager = DataManager("file")
    
    # Save the raw (unmasked) data
    data_manager.save_data(test_data, filename="raw_data.txt")
    
    # Save the masked data
    data_manager.save_data(masked_data, filename="masked_data.txt")
    
    print("Dados originais salvos em raw_data.txt")
    print("Dados mascarados salvos em masked_data.txt")

if __name__ == "__main__":
    main()