from selenium.webdriver.common.by import By


class AdminPageLocators:

    STATUS_MESSAGE = (By.XPATH, "//div[@id='rightPanel']/p[@style='color: #080']/b")
    SUCCESS_MESSAGE = "Settings saved successfully."

    # Database Form
    DATABASE_INITIALIZE_BUTTON = (By.XPATH, "//div[@id='rightPanel']//button[@value='INIT']")
    DATABASE_CLEAN_BUTTON = (By.XPATH, "//div[@id='rightPanel']//button[@value='CLEAN']")

    # JMS Service Form
    JMS_SERVICE_STATUS_MESSAGE = (By.XPATH, "//div[@id='rightPanel']//form[@name='toggleJms']//td[@width='20%']")
    JMS_SERVICE_BUTTON = (By.XPATH, "//div[@id='rightPanel']//form[@name='toggleJms']//input[@class='button']")

    # Data Access Mode Form
    RADIO_BUTTON_SOAP = (By.XPATH, "//div[@id='rightPanel']//input[@id='accessMode1']")
    RADIO_BUTTON_REST_XML = (By.XPATH, "//div[@id='rightPanel']//input[@id='accessMode2']")
    RADIO_BUTTON_REST_JSON = (By.XPATH, "//div[@id='rightPanel']//input[@id='accessMode3']")
    RADIO_BUTTON_JDBC = (By.XPATH, "//div[@id='rightPanel']//input[@id='accessMode4']")

    # Web Service Form
    LINK_WSDL = (By.XPATH, "//div[@id='rightPanel']//a[@href='services/ParaBank?wsdl'][text()='WSDL']")
    LINK_WADL = (By.XPATH, "//div[@id='rightPanel']//a[@href='services/bank?_wadl&_type=xml'][text()='WADL']")
    LINK_SWAGGER = (By.XPATH, "//div[@id='rightPanel']//a[@href='/parabank/api-docs/index.html'][text()='SWAGGER']")
    LINK_LOAN_WSDL = (By.XPATH, "//div[@id = 'rightPanel']//a[@href='services/LoanProcessor?wsdl'][text()='WSDL']")

    INPUT_SOAP_ENDPOINT = (By.XPATH, "//div[@id='rightPanel']//input[@id='soapEndpoint']")
    INPUT_REST_ENDPOINT = (By.XPATH, "//div[@id='rightPanel']//input[@id='restEndpoint']")
    INPUT_ENDPOINT = (By.XPATH, "//div[@id='rightPanel']//input[@id='endpoint']")

    # Application Settings Form
    INPUT_INIT_BALANCE = (By.XPATH, "//div[@id='rightPanel']//input[@id='initialBalance']")
    INPUT_MIN_BALANCE = (By.XPATH, "//div[@id='rightPanel']//input[@id='minimumBalance']")
    DROPDOWN_LOAN_PROVIDER = (By.XPATH, "//div[@id='rightPanel']//select[@id='loanProvider']")
    DROPDOWN_LOAN_PROCESSOR = (By.XPATH, "//div[@id='rightPanel']//select[@id='loanProcessor']")
    INPUT_THRESHOLD = (By.XPATH, "//div[@id='rightPanel']//input[@id='loanProcessorThreshold']")
    ERROR = (By.XPATH, "//div[@id = 'rightPanel']//span[@class='error']")

    SUBMIT_BUTTON = (By.XPATH, "//div[@id='rightPanel']//input[@class='button'][@value='Submit']")
