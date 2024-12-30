class Savings:
    @staticmethod
    def calculate_post_tax_savings(savings, post_tax=True, tax_rate=0.1, return_tax=False):
        """
        Calculate the post-tax savings.
        If post_tax is False, apply the specified tax rate to the savings.
        If return_tax is True, return both the post-tax savings and the tax paid.
        """
        if not post_tax:
            tax_paid = savings * tax_rate  # Calculate tax
            post_tax_savings = savings * (1 - tax_rate)  # Apply tax
            if return_tax:
                return post_tax_savings, tax_paid
            return post_tax_savings
        if return_tax:
            return savings, 0
        return savings