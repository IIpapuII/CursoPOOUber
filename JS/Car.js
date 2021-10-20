function Car(license,drive){
    this.id;
    this.license = license;
    this.driver = drive;
    this.passenger;

   
}
Car.prototype.prinDataCar = function(){
    console.log(this.driver)
    console.log(this.drive.name)
    console.log(this.driver.document)
}