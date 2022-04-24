class Car{
    Integer id;
    String license;
    String driver;
    Integer passegenger;

    
    public Car(String license, Account driver){
        // diferencia la variable local con el atributo
        // con la palabra reservada this
        // con this tenemos haceso a los metosdos y variables de la clase
        this.license = license;
        this.driver = driver;

    }
    // un metodo para que me impriman los datos de esta clase
    void printlnDataCar(){
        System.out.println("License: " + license + " Driver: " + driver.name);
    }
}