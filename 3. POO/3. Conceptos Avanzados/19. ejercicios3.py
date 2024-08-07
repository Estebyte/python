class Fighter:
    def __init__(self, name, power, skills,):
        self.name = name
        self.power = power
        self.skills = skills
        self.is_fused = False

    def __add__(self, other):
        try:
            if self.is_fused or other.is_fused:
                raise Exception("It's not possible to fuse if a fighter is already a fusion")
        except Exception as error:
                print(error)
                return None

        new_name = self.name[:-2] + other.name[2:]
        new_power = ((self.power + other.power)//2)**2
        new_skills = (self.skills, other.skills)
        new_fighter = Fighter(new_name, new_power, new_skills)
        new_fighter.is_fused = True
        return new_fighter 
            
    
    def __repr__(self):
        return f"Fighter('{self.name}', {self.power}, {self.skills})"

goku = Fighter("Goku", 20, "Kame Hame Ha")       
vegeta = Fighter("Vegeta", 21, "Galick Ho")
bills = Fighter("Bills", 1000, "Hakai")
print(vegeta)
print(vegeta.is_fused)

gogeta = goku + vegeta
print(gogeta)
print(gogeta.is_fused)

bills_vegeta = bills + vegeta
print(bills_vegeta)
print(bills_vegeta.is_fused)


