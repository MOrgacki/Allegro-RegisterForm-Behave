class formClass:
    def enter_email:
        context.driver.find_element_by_id("email").send_keys(parameters['E-mail'])