class DataMasker:
    def __init__(self):
        pass

    def mask_data(self, data):
        """
        Anonymizes sensitive information in the provided data.
        
        Args:
            data (dict): The data containing sensitive information to be masked.
        
        Returns:
            dict: The masked data with sensitive information anonymized.
        """
        masked_data = data.copy()
        
        # Example masking logic
        if 'email' in masked_data:
            masked_data['email'] = self._mask_email(masked_data['email'])
        if 'telefone' in masked_data:
            masked_data['telefone'] = self._mask_phone(masked_data['telefone'])
        if 'cpf' in masked_data:
            masked_data['cpf'] = self._mask_cpf(masked_data['cpf'])
        
        return masked_data

    def _mask_email(self, email):
        """
        Masks the email address by replacing the local part with '****'.
        
        Args:
            email (str): The email address to be masked.
        
        Returns:
            str: The masked email address.
        """
        local_part, domain = email.split('@')
        return f'****@{domain}'

    def _mask_phone(self, phone):
        """
        Masks the phone number by replacing the last four digits with '****'.
        
        Args:
            phone (str): The phone number to be masked.
        
        Returns:
            str: The masked phone number.
        """
        return f'****{phone[-4:]}'

    def _mask_cpf(self, cpf):
        """
        Masks the CPF by replacing the first 6 digits with asterisks.
        
        Args:
            cpf (str): The CPF to be masked.
        
        Returns:
            str: The masked CPF.
        """
        return f'******{cpf[-5:]}'