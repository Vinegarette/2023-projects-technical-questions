import express from 'express';

// location is the simple (x, y) coordinates of an entity within the system
// spaceCowboy models a cowboy in our super amazing system
// spaceAnimal models a single animal in our amazing system
type location = { x: number, y: number };
type spaceCowboy = { name: string, lassoLength: number };
type spaceAnimal = { type: "pig" | "cow" | "flying_burger" };

// spaceEntity models an entity in the super amazing (ROUND UPPER 100) system
type spaceEntity =
    | { type: "space_cowboy", metadata: spaceCowboy, location: location }
    | { type: "space_animal", metadata: spaceAnimal, location: location };


// === ADD YOUR CODE BELOW :D ===

// === ExpressJS setup + Server setup ===
const spaceDatabase = [] as spaceEntity[];
const app = express();
app.use(express.json());

// the POST /entity endpoint adds an entity to your global space database
app.post('/entity', (req, res) => {
    const entities = req.body;
    spaceDatabase.push(...entities.entities);
    res.status(200);
    return res.send("Succesfully added entities to spaceDatabase!");
});

// Helper function to determine if an animal is lassoable.
function is_lassoable(cowboy: spaceEntity, animal: spaceEntity): boolean {
    let cowboy_data = cowboy.metadata as spaceCowboy;
    const lasso_length = cowboy_data.lassoLength;
    const c_l = cowboy.location;
    const a_l = animal.location;
    return lasso_length >= Math.sqrt(Math.pow((c_l.x - a_l.x), 2) + Math.pow((c_l.y - a_l.y), 2));
}

// lassoable returns all the space animals a space cowboy can lasso given their name
app.get('/lassoable', (req, res) => {
    // TODO: fill me in
    const name = req.body.cowboy_name;
    const cowboy: spaceEntity = spaceDatabase.find(entity => entity.type === "space_cowboy" && entity.metadata.name === name) as spaceEntity;

    if (cowboy === undefined) {
        res.status(400);
        return res.send(`No cowboy matching the given name ${name}`);
    }

    const animals: any[] = [];
    for (const e of spaceDatabase) {
        if (e.type === "space_animal" && is_lassoable(cowboy, e) === true) {
            animals.push({
                "type": e.metadata.type,
                "location": e.location
            });
        }
    }

    const result = { "space_animals": animals };
    console.log(result);
    res.status(200);
    return res.send("Bruh");
})

app.listen(8080);
