Marcas:

using System;
using System.Collections.Generic;
using System.Linq;

class Vehicle
{
    public string Marca { get; set; }
    public string Modelo { get; set; }
    public string Combustible { get; set; }
}

class Program
{
    static void Main()
    {
        var vehicles = new List<Vehicle>
        {
            new Vehicle { Marca = "Toyota", Modelo = "Corolla", Combustible = "Gasolina" },
            new Vehicle { Marca = "Honda", Modelo = "Civic", Combustible = "Gasolina" },
            new Vehicle { Marca = "Ford", Modelo = "Focus", Combustible = "Gasolina" },
            new Vehicle { Marca = "Chevrolet", Modelo = "Malibu", Combustible = "Gasolina" },
            new Vehicle { Marca = "Nissan", Modelo = "Altima", Combustible = "Gasolina" },
            new Vehicle { Marca = "BMW", Modelo = "X5", Combustible = "Diesel" },
            new Vehicle { Marca = "Audi", Modelo = "A4", Combustible = "Gasolina" },
            new Vehicle { Marca = "Mercedes-Benz", Modelo = "C-Class", Combustible = "Gasolina" },
            new Vehicle { Marca = "Volkswagen", Modelo = "Golf", Combustible = "Gasolina" },
            new Vehicle { Marca = "Hyundai", Modelo = "Elantra", Combustible = "Gasolina" },
            new Vehicle { Marca = "Kia", Modelo = "Sorento", Combustible = "Gasolina" },
            new Vehicle { Marca = "Mazda", Modelo = "CX-5", Combustible = "Gasolina" },
            new Vehicle { Marca = "Subaru", Modelo = "Outback", Combustible = "Gasolina" },
            new Vehicle { Marca = "Tesla", Modelo = "Model S", Combustible = "Eléctrico" },
            new Vehicle { Marca = "Volvo", Modelo = "XC90", Combustible = "Gasolina" },
            new Vehicle { Marca = "Lexus", Modelo = "RX", Combustible = "Gasolina" },
            new Vehicle { Marca = "Jaguar", Modelo = "F-Pace", Combustible = "Gasolina" },
            new Vehicle { Marca = "Land Rover", Modelo = "Range Rover", Combustible = "Diesel" },
            new Vehicle { Marca = "Porsche", Modelo = "Cayenne", Combustible = "Gasolina" },
            new Vehicle { Marca = "Ferrari", Modelo = "488", Combustible = "Gasolina" },
            new Vehicle { Marca = "Lamborghini", Modelo = "Huracan", Combustible = "Gasolina" },
            new Vehicle { Marca = "Maserati", Modelo = "Levante", Combustible = "Gasolina" },
            new Vehicle { Marca = "Bentley", Modelo = "Bentayga", Combustible = "Gasolina" },
            new Vehicle { Marca = "Rolls-Royce", Modelo = "Phantom", Combustible = "Gasolina" },
            new Vehicle { Marca = "Aston Martin", Modelo = "DBX", Combustible = "Gasolina" },
            new Vehicle { Marca = "McLaren", Modelo = "720S", Combustible = "Gasolina" },
            new Vehicle { Marca = "Bugatti", Modelo = "Chiron", Combustible = "Gasolina" },
            new Vehicle { Marca = "Pagani", Modelo = "Huayra", Combustible = "Gasolina" },
            new Vehicle { Marca = "Koenigsegg", Modelo = "Jesko", Combustible = "Gasolina" },
            new Vehicle { Marca = "Rimac", Modelo = "C_Two", Combustible = "Eléctrico" }
        };

        // Contar marcas únicas y ordenarlas
        var marcasDistintas = vehicles.Select(v => v.Marca).Distinct().OrderBy(m => m).ToList();
        
        Console.WriteLine($"Número de marcas distintas: {marcasDistintas.Count}");
        Console.WriteLine("Marcas ordenadas de la A a la Z:");
        
        foreach (var marca in marcasDistintas)
        {
            Console.WriteLine(marca);
        }
    }
}


Inventario:

using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static void Main()
    {
        var productos = new List<(string nombre, string tipo, int cantidad)>
        {
            ("asparagus", "vegetables", 5),
            ("banana", "fruits", 30),
            ("limon", "fruits", 13),
            ("mango", "fruits", 10),
        };

        var productoMayorExistencia = productos.OrderByDescending(p => p.cantidad).First();
        Console.WriteLine($"Producto con mayor existencia: {productoMayorExistencia.nombre}, Cantidad: {productoMayorExistencia.cantidad}");
    }
}





Heroes:

using System;
using System.Collections.Generic;
using System.Linq;

class Hero
{
    public string Name { get; set; }
    public string City { get; set; }
    public string Power { get; set; }
    public string Type { get; set; }
}

class Program
{
    static void Main()
    {
        var heroes = new List<Hero>
        {
            new Hero { Name = "Superman", City = "Metropolis", Power = "Super strength, flight, x-ray vision", Type = "Alien" },
            new Hero { Name = "Batman", City = "Gotham", Power = "Peak human condition, martial arts, detective skills", Type = "Human" },
            new Hero { Name = "Wonder Woman", City = "Themyscira", Power = "Super strength, agility, combat skills", Type = "Demigod" },
            new Hero { Name = "Spider-Man", City = "New York", Power = "Wall-crawling, spider-sense, agility", Type = "Mutated Human" },
            new Hero { Name = "Iron Man", City = "New York", Power = "Genius intellect, powered armor suit", Type = "Human" },
            new Hero { Name = "Thor", City = "Asgard", Power = "God of Thunder, super strength, control over lightning", Type = "God" },
            new Hero { Name = "Hulk", City = "New York", Power = "Super strength, invulnerability", Type = "Mutated Human" },
            new Hero { Name = "Black Widow", City = "Stalingrad", Power = "Expert martial artist, spy skills", Type = "Human" },
            new Hero { Name = "Captain America", City = "Brooklyn", Power = "Super strength, agility, expert tactician", Type = "Enhanced Human" },
            new Hero { Name = "Flash", City = "Central City", Power = "Super speed", Type = "Mutated Human" },
            new Hero { Name = "Green Lantern", City = "Coast City", Power = "Power ring with various abilities", Type = "Human" },
            new Hero { Name = "Aquaman", City = "Atlantis", Power = "Underwater breathing, super strength, control over sea life", Type = "Atlantean" },
            new Hero { Name = "Doctor Strange", City = "New York", Power = "Mastery of magic, time manipulation", Type = "Human" },
            new Hero { Name = "Black Panther", City = "Wakanda", Power = "Enhanced strength, agility, advanced technology", Type = "Enhanced Human" },
            new Hero { Name = "Scarlet Witch", City = "Sokovia", Power = "Reality manipulation, telekinesis", Type = "Mutated Human" },
            new Hero { Name = "Vision", City = "New York", Power = "Density manipulation, super strength, flight", Type = "Android" },
            new Hero { Name = "Ant-Man", City = "San Francisco", Power = "Size manipulation, communication with insects", Type = "Human" },
            new Hero { Name = "Wasp", City = "San Francisco", Power = "Size manipulation, flight, bio-electric energy blasts", Type = "Human" },
            new Hero { Name = "Hawkeye", City = "Waverly", Power = "Expert marksman, martial artist", Type = "Human" },
            new Hero { Name = "Star-Lord", City = "Missouri", Power = "Expert pilot, marksman, enhanced durability", Type = "Human/Celestial Hybrid" }
        };

        var ciudadCount = heroes.GroupBy(h => h.City)
                                .Select(g => new { City = g.Key, Count = g.Count() })
                                .OrderByDescending(g => g.Count)
                                .First();

        Console.WriteLine($"La ciudad con más héroes es: {ciudadCount.City}, con {ciudadCount.Count} héroes.");
    }
}


personas:

using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        var personas = new List<Person>
        {
            new Person { Id = 1, Name = "Juan", Edad = 30, Sexo = "Masculino" },
            new Person { Id = 2, Name = "Pedro", Edad = 25, Sexo = "Masculino" },
            new Person { Id = 3, Name = "María", Edad = 28, Sexo = "Femenino" },
            new Person { Id = 4, Name = "Ana", Edad = 22, Sexo = "Femenino" },
            new Person { Id = 5, Name = "Luis", Edad = 35, Sexo = "Masculino" },
            new Person { Id = 6, Name = "Sofía", Edad = 27, Sexo = "Femenino" },
            new Person { Id = 7, Name = "Carlos", Edad = 32, Sexo = "Masculino" },
            new Person { Id = 8, Name = "Laura", Edad = 26, Sexo = "Femenino" },
            new Person { Id = 9, Name = "Jorge", Edad = 29, Sexo = "Masculino" },
            new Person { Id = 10, Name = "Marta", Edad = 24, Sexo = "Femenino" },
            new Person { Id = 11, Name = "Andrés", Edad = 31, Sexo = "Masculino" },
            new Person { Id = 12, Name = "Elena", Edad = 23, Sexo = "Femenino" },
            new Person { Id = 13, Name = "Miguel", Edad = 34, Sexo = "Masculino" },
            new Person { Id = 14, Name = "Lucía", Edad = 21, Sexo = "Femenino" },
            new Person { Id = 15, Name = "Fernando", Edad = 33, Sexo = "Masculino" },
            new Person { Id = 16, Name = "Isabel", Edad = 30, Sexo = "Femenino" },
            new Person { Id = 17, Name = "Ricardo", Edad = 28, Sexo = "Masculino" },
            new Person { Id = 18, Name = "Patricia", Edad = 27, Sexo = "Femenino" },
            new Person { Id = 19, Name = "Roberto", Edad = 26, Sexo = "Masculino" },
            new Person { Id = 20, Name = "Gabriela", Edad = 25, Sexo = "Femenino" },
            new Person { Id = 21, Name = "Alberto", Edad = 24, Sexo = "Masculino" },
            new Person { Id = 22, Name = "Verónica", Edad = 23, Sexo = "Femenino" },
            new Person { Id = 23, Name = "Daniel", Edad = 22, Sexo = "Masculino" },
            new Person { Id = 24, Name = "Natalia", Edad = 21, Sexo = "Femenino" },
            new Person { Id = 25, Name = "Francisco", Edad = 35, Sexo = "Masculino" },
            new Person { Id = 26, Name = "Carmen", Edad = 34, Sexo = "Femenino" },
            new Person { Id = 27, Name = "Héctor", Edad = 33, Sexo = "Masculino" },
            new Person { Id = 28, Name = "Alicia", Edad = 32, Sexo = "Femenino" },
            new Person { Id = 29, Name = "Sergio", Edad = 31, Sexo = "Masculino" },
            new Person { Id = 30, Name = "Paula", Edad = 30, Sexo = "Femenino" }
        };

        int totalEdad = 0;
        foreach (var persona in personas)
        {
            totalEdad += persona.Edad;
        }

        double promedioEdad = (double)totalEdad / personas.Count;

        Console.WriteLine($"La suma de las edades es: {totalEdad}");
        Console.WriteLine($"El promedio de las edades es: {promedioEdad}");
    }
}

class Person
{
    public int Id { get; set; }
    public string Name { get; set; }
    public int Edad { get; set; }
    public string Sexo { get; set; }
}
