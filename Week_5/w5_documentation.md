START
    // Define price constants
    SET COFFEE_PRICE = 8.50
    SET TEA_PRICE = 6.00
    SET SANDWICH_PRICE = 12.00

    // Get Inputs
    INPUT customer_name
    INPUT coffee_qty
    INPUT tea_qty
    INPUT sandwich_qty

    // Calculation Function Logic
    FUNCTION calculate_total(coffee_qty, tea_qty, sandwich_qty)
        total = (coffee_qty * COFFEE_PRICE) + (tea_qty * TEA_PRICE) + (sandwich_qty * SANDWICH_PRICE)
        RETURN total
    ENDFUNCTION

    // Output Function Logic
    FUNCTION print_receipt(name, coffee_qty, tea_qty, sandwich_qty, total_amount)
        PRINT "===== RECEIPT ====="
        PRINT "Customer : " + name
        PRINT "Coffee   : " + coffee_qty
        PRINT "Tea      : " + tea_qty
        PRINT "Sandwich : " + sandwich_qty
        PRINT "-------------------"
        PRINT "Total = RM " + Formatted(total_amount)
    ENDFUNCTION

    // Main Execution Flow
    SET bill_total = calculate_total(coffee_qty, tea_qty, sandwich_qty)
    CALL print_receipt(customer_name, coffee_qty, tea_qty, sandwich_qty, bill_total)
END