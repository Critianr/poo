class Main {
    public static void main(String[]args){
        System.out.println("Hola Mundo");
        Car car = new Car("AMQ123", new Account("Carlos H","AND123"));
        car.passegenger = 4;
        car.printlnDataCar();
    }
}