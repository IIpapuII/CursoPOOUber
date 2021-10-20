class Main{
    public static void main(String[] args) {
        System.out.println("Hola Mundo");
        Car car = new Car("AMQ123", new Account("Andres Herrera", "AMQ123"));
        
        car.passenger = 4;

        System.out.println("Car License: "+ car.license);
        
        car.printDataCar();

        }
}