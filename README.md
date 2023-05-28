# K12-Physics-S2_SY2223

A collection of formulas for Physics calculations

* Hardcover - [Physics: Problems and Solutions](https://www.amazon.com/gp/product/1601530552/)

## References

* [Mathematics in R Markdown](https://rpruim.github.io/s341/S19/from-class/MathinRmd.html)

---

## 1: Momentum

---

### 1.01: Semester Introduction

![image_1](1%20-%20Momentum/1-01%20-%20Semester%20Introduction/image_1.png)

---

### 1.02: Linear Momentum and Impulse

![image_1](1%20-%20Momentum/1-02%20-%20Linear%20Momentum%20and%20Impulse/image_1.png)

![image_2](1%20-%20Momentum/1-02%20-%20Linear%20Momentum%20and%20Impulse/image_2.png)

![image_3](1%20-%20Momentum/1-02%20-%20Linear%20Momentum%20and%20Impulse/image_3.png)

---

1. Suppose a 1,650 kg car is traveling at 15.0 m/s. Find the average force that is needed to stop the car in 4.0 s.

* What information are you given?

```js
// D is capital delta (Δ)
m = 1,650 kg
vi = 15.0 m/s
Dt = 4.0 s
```

* Find the initial momentum and final momentum.

```js
// D is capital delta (Δ)
// pi = m*v
let m = 1650; // kg
let v = 15.0; // m/s
let pi = m * v; // kg * m / s
console.log('pi =', pi, 'kg * m / s');
// pi = 24750 kg * m / s
let pf = 0; // kg * m / s
console.log('pf =', pf, 'kg * m / s');
// pf = 0 kg * m / s
let Dp = pf - pi; // kg * m / s
console.log('Dp =', Dp, 'kg * m / s');
// Dp = -24750 kg * m / s
```

* Use the impulse-momentum theorem to solve for the force and round to the correct number of significant figures.

```js
// D is capital delta (Δ)
let m = 1650; // kg
let v = 15.0; // m/s
let pi = m * v; // kg * m / s
let pf = 0; // kg * m / s
let Dp = pf - pi; // kg * m / s
let Dt = 4.0; // s
// F * Dt = Dp
// F = Dp / Dt
let F = Dp / Dt; // N
console.log('F =', F, 'N')
// F = -6187.5 N
console.log('F =', Math.round(F / Math.pow(10, 2)) * Math.pow(10, 2), 'N')
// F = -6200 N
```

---

2. A baseball with a mass of 0.145 kg approaches a bat at 45 m/s. After the bat hits the ball, the ball leaves the bat moving in the opposite direction at 50.0 m/s. Find the impulse and, using the force vs. time graph, the average force exerted by the bat. The time of the impulse can be determined from the graph. Dt = 0.001 s

* What information are you given?

```js
m = 0.145 kg
vi = 45 m/s
vf = −50.0 m/s
Dt = 0.001 s
```

* Write equations for the initial and final momenta.

```
p = m * v
pi = m * vi
pf = m * vf
```

* Solve for initial and final momenta.

```js
// D is capital delta (Δ)
let m = 0.145; // kg
let vi = 45; // m/s
let vf = -50.0; // m/s
let pi = m * vi; // kg * m / s
console.log('pi =', pi, 'kg * m / s');
// pi = 6.5249999999999995 kg * m / s
let pf = m * vf; // kg * m / s
console.log('pf =', pf, 'kg * m / s');
// pf = -7.249999999999999 kg * m / s
let Dp = pf - pi; // kg * m / s
console.log('Dp =', Dp, 'kg * m / s');
// Dp = -13.774999999999999 kg * m / s
console.log('impulse = Dp =', Math.round(Dp * Math.pow(10, 3)) / Math.pow(10, 3), 'kg * m / s');
// impulse = Dp = -13.775 kg * m / s
console.log('impulse = Dp =', Math.round(Dp), 'kg * m / s');
// impulse = Dp = -14 kg * m / s
```

* Find the average force.

```js
let m = 0.145; // kg
let vi = 45; // m/s
let vf = -50.0; // m/s
let pi = m * vi; // kg * m / s
let pf = m * vf; // kg * m / s
let Dp = pf - pi; // kg * m / s
let Dt = 0.001; // s
// F * Dt = Dp
// F = Dp / Dt
let F = Dp / Dt; // N
console.log('F =', F, 'N')
// F = -13774.999999999998 N
console.log('F =', Math.round(F / Math.pow(10, 3)) * Math.pow(10, 3), 'N')
// F = -14000 N
```
---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 38

---

### 1.03: Law of Conservation of Momentum

![image_1](/1%20-%20Momentum/1-03%20-%20Law%20of%20Conservation%20of%20Momentum/image_1.png)

```
pi == pf
```

---

1. An 8,500 kg train car moves at 12.0 m/s until it bumps into a stationary 8,500 kg car and latches onto it. What is the speed of the two cars linked together?

* What information is known?

```
m1 = 8500 kg
m2 = 8500 kg
Vi = 12.0 m/s
Vf = ? m/s
```
* Write what you know in equation form.

```
initial momentum = final momentum, or total pf = total pi
(m1 + m2) * Vf = m1 * Vi
Vf = (m1 / (m1 + m2)) * Vi
```

* Substitute and solve for final velocity.

```js
let m1 = 8500; // kg
let m2 = 8500; // kg
let Vi = 12.0; // m/s
let Vf = (m1/(m1+m2)) * Vi; // m/s
console.log('Vf =', Vf, 'm/s');
// Vf = 6 m/s
```

---

2. An astronaut adrift in space with no velocity throws a 38 kg wrench at 13 m/s. The mass of the astronaut with the remaining equipment is 165 kg. Find the velocity of the astronaut after she releases the wrench.

* What information is known?

```
Mass Wrench = Mw = 38 kg
Mass Astronaut = Ma = 165 kg
Vi = 0 m/s
Velocity Wrench = Vw = 13 m/s
Velocity Astronaut = Va = ?
```

* Find the astronaut’s final momentum.

```js
let Mw = 38; // kg
let Ma = 165; // kg
let Vw = 13; // m/s
// total momentum = pt
// pa = momentum of astronaut
// pw = momentum of wrench
// pt = pa + pw
// 0 = (Ma * Va) + (Mw * Vw)
let Va = -Mw * Vw / Ma; // m/s
console.log('Va =', Va, 'm/s');
// -2.993939393939394 m/s
console.log('Va =', Math.round(Va), 'm/s');
// Va = -3 m/s
```

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 39

---

### 1.04 Momentum in Collisions

![image_1](1%20-%20Momentum/1-04%20-%20Momentum%20in%20Collisions/image_1.png)

---

1. Two carts are at rest and a spring is attached to one of the carts. The spring is used to propel the carts away from one another. The carts have masses of 1.2 kg and 2.5 kg. The 2.5 kg cart (Cart B) has a velocity of 1.5 m/s after they spring apart. Find the velocity of the 1.2 kg cart.

* What information is known?

```
Cart A: mass = 1.2 kg, final velocity = ?
Cart B: mass = 2.5 kg, final velocity = +1.5 m/s
No net external force acts, so the total momentum is still zero after the force between the carts pushes them apart.
```

* Apply the law of conservation of momentum.

```
Initially, the total momentum is 0 kg•m/s, so the final momentum is also 0 kg•m/s. The carts may be moving, but the momentum vectors will be in opposite directions.

Designate the final velocities vA and vB and write an equation:

total momentum after = total momentum before

(Mass of A) * (Velocity of A) + (Mass of B) * (Velocity of B) = 0

Ma * Va + Mb * Vb = 0
```

* Solve for Va.

```js
let Ma = 1.2; // kg
let Mb = 2.5; // kg
let Vb = 1.5; // m/s
let Va = (-Mb * Vb) / Ma;
console.log('Va =', Va, 'm / s');
// Va = -3.125 m / s

console.log('Va =', Math.round(Va * Math.pow(10, 1)) / Math.pow(10, 1), 'm / s');
// Va = -3.1 m / s
```

---

2. Object A, a smooth metal disk, has a mass of 1.0 kg. It slides on ice at 1.0 m/s directly into a 0.50 kg smooth metal disk at rest, Object B, which then moves at 1.33 m/s along the same straight line. Find the final velocity of Object A. Assume that no energy is lost as heat or sound during the collision.

* What information is given?

```
Before collision:
Object A: mass Ma = 1.00 kg, initial velocity iVa = 1.0 m/s
Object B: mass Mb = 0.50 kg, initial velocity iVb = 0.0 m/s

After collision:
Object A: final velocity fVa = ?
Object B: final velocity fVb = 1.33 m/s
```

* Use the law of conservation of momentum.

```
momentum final = momentum initial
Ma*fVa + Mb*fVb = Ma*iVa + Mb*iVb
```

* Solve for fVa, insert values into the equation, and calculate.

```js
let Ma = 1.00; // kg
let iVa = 1.0; // m/s
let Mb = 0.50; // kg
let iVb = 0.0; // kg
let fVb = 1.33; // m/s
let fVa = (Ma*iVa + Mb*iVb - Mb*fVb) / Ma; // m/s
console.log('fVa =', fVa, 'm/s');
// fVa = 0.33499999999999996 m/s
// subtract EPSILON to avoid float rounding error
console.log('fVa =', Math.round((fVa - Number.EPSILON) * Math.pow(10, 2)) / Math.pow(10, 2), 'm/s');
// fVa = 0.33 m/s
```

---

3. A 1,450 kg car is traveling east at 15.0 m/s while a 1,650 kg car is traveling north toward the same intersection at 20.0 m/s. The cars crash and stick together. What is the velocity of the conjoined cars immediately after the collision? What is the angle at which the conjoined cars move?

* What information is given?

```
Before collision:
Object A: mass Ma = 1,450 kg, initial velocity iVa = 15.0 m/s
Object B: mass Mb = 1,650 kg, initial velocity iVb = 20.0 m/s

After collision:
Object A: final velocity fVa = 0.0 m/s
Object B: final velocity fVb = 0.0 m/s
```

* Find the initial momentum for all x components.

```js
// final momentum of x-component
// pfx = pAi
// pfx = Ma * iVa
let Ma = 1450; // kg
let iVa = 15.0; // m/s
let pfx = Ma * iVa
console.log('pfx =', pfx, 'kg * m/s');
// pfx = 21750 kg * m/s
```

* Find the initial momentum for all y components.

```js
// final momentum of y-component
// pfy = pBi
// pfy = Mb * iVb
let Mb = 1650; // kg
let iVb = 20.0; // m/s
let pfy = Mb * iVb
console.log('pfy =', pfy, 'kg * m/s');
// pfy = 33000 kg * m/s
```

* Find the magnitude of the final momentum.

```js
let Ma = 1450; // kg
let iVa = 15.0; // m/s
let pfx = Ma * iVa
let Mb = 1650; // kg
let iVb = 20.0; // m/s
let pfy = Mb * iVb
// final momentum
let Pf = Math.sqrt(Math.pow(pfx, 2) + Math.pow(pfy, 2));
console.log('Pf =', Pf, 'kg * m/s')
// Pf = 39522.93637876619 kg * m/s
console.log('Pf =', Math.round(Pf / Math.pow(10, 2)) * Math.pow(10, 2), 'kg * m/s')
// Pf = 39500 kg * m/s
```

* Find the magnitude of the final velocity.

```js
// Pf = Mf * Vf
// Vf = Pf / Mf
let Mf = Ma + Mb; // kg
let Vf = Pf / Mf; // m/s
console.log('Vf =', Vf, 'm/s');
// Vf = 12.74933431573103 m/s
console.log('Vf =', Math.round(Vf * Math.pow(10, 1)) / Math.pow(10, 1), 'm/s');
// Vf = 12.7 m/s
```

* Find the direction of the final velocity.

```js
// cos(theta) = pfx / Pf
let theta = Math.acos(pfx / Pf);
let degrees = theta * 180 / Math.PI;
console.log('degrees =', degrees, 'degrees');
// degrees = 56.611486423888486 degrees
console.log('degrees =', Math.round(degrees * Math.pow(10, 1)) / Math.pow(10, 1), 'degrees');
// degrees = 56.6 degrees
```

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 40 and 41

---

### 1.08: Conservation of Angular Momentum

![image_1](1%20-%20Momentum/1-08%20-%20Conservation%20of%20Angular%20Momentum/image_1.png)

![image_2](1%20-%20Momentum/1-08%20-%20Conservation%20of%20Angular%20Momentum/image_2.png)

![image_3](1%20-%20Momentum/1-08%20-%20Conservation%20of%20Angular%20Momentum/image_3.png)

![image_4](1%20-%20Momentum/1-08%20-%20Conservation%20of%20Angular%20Momentum/image_4.png)

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 42

---

1. Which of the following objects would have a greater angular momentum (L): a 0.15 kg hollowed can attached to a 4.0 m string, spun at an angular velocity of 15 rad/s; or a 0.15 kg hollowed can attached to a 6.0 m string, spun at a rotational velocity of 15 rad/s?

```js
// L = m * r^2 * w

let m1 = 0.15; // kg
let r1 = 4.0; // m
let w1 = 15; // rad/s
let L1 = m1 * Math.pow(r1, 2) * w1; // kg * m^2/s
console.log('L1 =', L1, 'kg * m^2/s');
// L1 = 36 kg * m^2/s

let m2 = 0.15; // kg
let r2 = 6.0; // m
let w2 = 15; // rad/s
let L2 = m2 * Math.pow(r2, 2) * w2; // kg * m^2/s
console.log('L2 =', L2, 'kg * m^2/s');
// L2 = 80.99999999999999 kg * m^2/s
console.log('L2 =', Math.round(L2), 'kg * m^2/s');
// L2 = 81 kg * m^2/s
```

---

## 2: Work

---

### 2.01: Work and Power

![image_1](2%20-%20Work/2-01%20-%20Work%20and%20Power/image_1.png)

![image_2](2%20-%20Work/2-01%20-%20Work%20and%20Power/image_2.jpg)

![image_3](2%20-%20Work/2-01%20-%20Work%20and%20Power/image_3.png)

![image_4](2%20-%20Work/2-01%20-%20Work%20and%20Power/image_4.png)

Kinetic Energy = 1/2 * mass * velocity ^ 2

![image_5](2%20-%20Work/2-01%20-%20Work%20and%20Power/image_5.png)

![image_6](2%20-%20Work/2-01%20-%20Work%20and%20Power/image_6.png)

![image_7](2%20-%20Work/2-01%20-%20Work%20and%20Power/image_7.png)

---

1. A weightlifter lifts a 100 kg barbell 2.0 m from the ground in 2.0 s. How much work has he done? What is the power of the lift?

List the given quantities.

```js
let m = 100; // kg
let g = 9.8; // m/s^2
let d = 2.0; // m
let t = 2.0; // s
```

Identity what you are looking for.

```
W = ?
P = ?
```

Calculate work.

```js
let m = 100; // kg
let g = 9.8; // m/s^2
let d = 2.0; // m
// W = Fnet * d
// Fg = m * g
let W = m * g * d; // J
console.log('W =', W, 'J');
// W = 1960.0000000000002 J
console.log('W =', Math.round(W), 'J');
// W = 1960 J
console.log('W =', W.toPrecision(2), 'J');
// W = 2.0e+3 J
```

Calculate power.

```js
let m = 100; // kg
let g = 9.8; // m/s^2
let d = 2.0; // m
let W = m * g * d; // J
let t = 2.0; // s
let P = W.toPrecision(2) / t; // W
console.log('P =', P, 'W');
// P = 1000 W
```
---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 43

---

### 2.02: Direction of Force and Work

![image_1](2%20-%20Work/2-02%20-%20Direction%20of%20Force%20and%20Work/image_1.jpg)

---

1. A sailor pulls a boat full of cargo using a rope angled at 60.0 degrees. The sailor applies 1.00 × 10^3 N of force and pulls the boat for 30.0 m to the end of the dock. How much work does the sailor do?

What do you know?

```js
let Fa = Math.pow(10, 3); // N
let degrees = 60.0; // degrees
let radians = degrees * Math.PI / 180; // radians
let d = 30.0; // m
```

What are you trying to find?

```
W = ?
```

Draw a free-body diagram and identify the forces. Apply Newton’s second law.

![image_2](2%20-%20Work/2-02%20-%20Direction%20of%20Force%20and%20Work/image_2.png)

```
Fa is the force the sailor applies to the rope.
Fa|| is the force that is applied to the boat in the direction of the boat’s motion. Remember, we use Fa|| to mean the force that is parallel to motion.
```

Calculate work using only the components of forces that are in the direction of motion.

```js
let Fa = Math.pow(10, 3); // N
let degrees = 60.0; // degrees
let radians = degrees * Math.PI / 180; // radians
let d = 30.0; // m
// W = Fa * cos(radians) * d
let W = Fa * Math.cos(radians) * d;
console.log('W =', W, 'J');
// W = 15000.000000000004 J
console.log('W =', W.toPrecision(3), 'J');
// W = 1.50e+4 J
```

---

2. A sailor pushes a 50.0 kg barrel along a dock. He then pushes it up a 10.0 m gangplank to the deck of a ship. The sailor applies his force parallel to the dock. The gangplank makes an angle of 30.0 degrees with the dock. Assume that the gangplank is frictionless. How much work does the sailor do?

What do you know?

```js
let m = 50.0; // kg
let d = 10.0; // m
let degrees = 30.0; // degrees
let radians = degrees * Math.PI / 180; // radians
let g = 9.80; // m/s^2
// frictionless plank
// constant velocity
```

What are you trying to find?
```
W = ?
```

Draw a free-body diagram and identify the forces. Apply Newton’s second law.

![image_3](2%20-%20Work/2-02%20-%20Direction%20of%20Force%20and%20Work/image_3.jpg)

```
Fa|| = Fg||
Fg|| = m * g * sin(radians)
Fa|| = m * g * sin(radians)
```

Calculate work using only the components of forces that are in the direction of motion.

```js
let m = 50.0; // kg
let d = 10.0; // m
let degrees = 30.0; // degrees
let radians = degrees * Math.PI / 180; // radians
let g = 9.80; // m/s^2
// W = F * d
// W = Fa|| * d
let W = m * g * Math.sin(radians) * d; // J
console.log('W =', W, 'J');
// W = 2450 J
console.log('W =', W.toPrecision(2), 'J');
// W = 2.5e+3 J
```

---

3. A 70.0 kg sailor climbs an 11.5 m rope ladder to a mast above at constant velocity. The rope ladder forms an angle of 30.0 degrees with the mast. Assume that the ladder is frictionless. How much work does the sailor do?

What do you know?

```js
let m = 70.0; // kg 
let d = 11.5; // m
let degrees = 30.0;
let radians = degrees * Math.PI / 180; // radians
let G = radians; // radians
let g = 9.80; // m/s^2
// frictionless ladder
// constant velocity
```

What are you trying to find?

```
W = ?
```

Draw a free-body diagram and identify the forces.

![image_4](2%20-%20Work/2-02%20-%20Direction%20of%20Force%20and%20Work/image_4.jpg)

```
Remember that work is determined by using only the force that is applied in the direction of motion.
```

Apply Newton’s second law.

```
Fa|| = Fg||
Fg|| = m * g * cos(radians)
Fa|| = m * g * cos(radians)
```

Calculate work using only the components of forces that are in the direction of motion.

```js
// W = F * d
// W = Fa|| * d
let m = 70.0; // kg 
let d = 11.5; // m
let degrees = 30.0;
let radians = degrees * Math.PI / 180; // radians
let G = radians; // radians
let g = 9.80; // m/s^2
let W = m * g * Math.cos(radians) * d; // J
console.log('W =', W, 'J');
// W = 6832.074410455438 J
console.log('W =', W.toPrecision(3), 'J');
// W = 6.83e+3 J
```

---

4. If wind at angle = 45 degrees exerts a force of 6.33 X 10^4 N on a ship, and the ship travels 1.00 X 10^3 m, then how much work did the wind do on the ship?

```js
let F = 6.33 * Math.pow(10, 4); // N
let d = Math.pow(10, 3); // m
let degrees = 45.0;
let radians = degrees * Math.PI / 180; // radians
let W = F * Math.cos(radians) * d; // J
console.log('W =', W, 'J');
// W = 44759859.24910846 J
console.log('W =', W.toPrecision(3), 'J');
// W = 4.48e+7 J
```

---

5. If the wind does work of 4.48 X 10^7 J on a sailing ship with a mass of 2.00 X 10^6 kg (like USS Constitution), then how fast will the ship’s speed increase? Assume the ship starts out with a velocity of 0 m/s.

Identify what you know?

```js
let W = 4.48 * Math.pow(10, 7); // J
let m = 2.00 * Math.pow(10, 6); // kg
```

What you are looking for.

```
Dv = ?
```

Identify the equation you will use.

```
W = DKE = 1/2 * m * Dv^2
```

Solve for the variable you are seeking and insert values into the equation.

```js
let W = 4.48 * Math.pow(10, 7); // J
let m = 2.00 * Math.pow(10, 6); // kg
let Dv = Math.sqrt(2 * W / m); // m/s
console.log('Dv =', Dv, 'm/s');
// Dv = 6.6932802122726045 m/s
console.log('Dv =', Dv.toPrecision(3), 'm/s');
// Dv = 6.69 m/s
```

---

![image_5](2%20-%20Work/2-02%20-%20Direction%20of%20Force%20and%20Work/image_5.png)

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 44

---

### 2.05: Machines and Mechanical Advantage

![image_1](2%20-%20Work/2-05%20-%20Machines%20and%20Mechanical%20Advantage/image_1.jpg)

![image_2](2%20-%20Work/2-05%20-%20Machines%20and%20Mechanical%20Advantage/image_2.png)

![image_3](2%20-%20Work/2-05%20-%20Machines%20and%20Mechanical%20Advantage/image_3.png)

![image_4](2%20-%20Work/2-05%20-%20Machines%20and%20Mechanical%20Advantage/image_4.png)

---

1. A Pilgrim raises a 50.0 N crate a distance of 10.0 m with a block and tackle. She exerts 25.0 N of force. What is the mechanical advantage of the block and tackle and how much rope does she have to pull? Assume this is an ideal machine.

What is given?

```js
let Fr = 50.0; // N
let Fe = 25.0; // N
let Dr = 10.0; // m
```

What are you trying to find?

```
MA = ? (Mechanical Advantage)
De = ?
```

What equations do you need, and are they in the right form?

```
MA = Fr / Fe
De = Dr * MA
```

Substitute values and solve for unknowns.

```js
let Fr = 50.0; // N
let Fe = 25.0; // N
let MA = Fr / Fe;
console.log('MA =', MA);
// MA = 2
console.log('MA =', MA.toPrecision(3));
// MA = 2.00

let Dr = 10.0; // m
let De = MA * Dr; // m
console.log('De =', De, 'm');
// De = 20 m
console.log('De =', De.toPrecision(3), 'm');
// De = 20.0 m
```

---

2. A Pilgrim farmer uses a lever to lift a 1,500 N rock. He exerts a force of 250 N and lifts the rock 0.15 m. If the efficiency of the lever is 85 percent, how far must he push down on the lever?

What is given?

```js
let Fr = 1500.0; // N
let Fe = 250.0; // N
let Dr = 0.15; // m
let eff = 0.85; // efficency
```

What are you trying to find?

```
De = ?
```

What equations do you need, and are they in the right form?

```
Work = Wo = Fr * dr
efficency = eff = Wo / W
De = Wo / (Fe * eff)
```

Substitute values and solve for unknowns.

```js
let Fr = 1500.0; // N
let Dr = 0.15; // m
let Wo = Fr * Dr; // J
console.log('Wo =', Wo, 'J');
// Wo = 225 J
let Fe = 250.0; // N
let eff = 0.85; // efficency
let De = Wo / (Fe * eff); // m
console.log('De =', De, 'm');
// De = 1.0588235294117647 m
console.log('De =', De.toPrecision(2), 'm');
// De = 1.1 m
```

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 45

---

## 3. Energy

---

### 3.01 Types of Energy and Their Conversions

![image_1](3%20-%20Energy/3-01%20-%20Types%20of%20Energy%20and%20Their%20Conversions/image_1.jpg)

![image_2](3%20-%20Energy/3-01%20-%20Types%20of%20Energy%20and%20Their%20Conversions/image_2.png)

```js
let c = 2.99792458 * Math.pow(10, 8); // m/s (speed of light can be rounded to 3.00 * Math.pow(10, 8)
// E = m * c^2
```


---

1. How much energy would be released if a 1.50 g bean could be converted entirely into energy?

Identify important information.

```js
let m = 1.50; // g;
m = m / 1000; // kg
let c = 2.99792458 * Math.pow(10, 8); // m/s
```

Calculate the energy.

```js
let m = 1.50; // g
m = m / 1000; // kg
let c = 2.99792458 * Math.pow(10, 8); // m/s
let E = m * Math.pow(c, 2); // J
console.log('E =', E, 'J');
// E = 134813276810522.64 J
console.log('E =', E.toPrecision(3), 'J');
// E = 1.35e+14 J
```

Analyze your result.

```
That’s a lot of energy from such a small amount of matter!
```

---

![image_3](3%20-%20Energy/3-01%20-%20Types%20of%20Energy%20and%20Their%20Conversions/image_3.jpg)

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 46

---

### 3.02: Kinetic and Potential Energy

![image_1](3%20-%20Energy/3-02%20-%20Kinetic%20and%20Potential%20Energy/image_1.jpg)

Kinetic Energy

```
K = KE = 1/2 * m * v^2
```

Potential Energy

```
Ug = PE = m * g * h
```

---
1. Suppose the spring in this spring-powered rifle has a spring constant of k = 920 N/m. How much elastic potential energy does it have, and how much work can it do in accelerating the projectile,if it is compressed by x = 0.10 m?

Identify the useful information

```js
let k = 920; // N/m
let x = 0.10; // m
```

Choose the appropriate equation.

* The potential energy of the compressed spring is also the amount of work it can do by decompressing. The potential energy of the spring compressed or stretched by a distance x is 1/2 * k * x^2 in terms of the spring constant k.

* Us = Potential Energy of the spring

Apply the appropriate equation.

```js
let k = 920; // N/m
let x = 0.10; // m
Us = 1/2 * k * Math.pow(x, 2); // J
console.log('Us =', Us, 'J');
// Us = 4.6000000000000005 J
console.log('Us =', Us.toPrecision(2), 'J');
// Us = 4.6 J
```

Express the answer.

```
The potential energy that the compressed spring stores is 4.6 J.
```

---

2. Use Newton’s laws and the laws of kinematics to find the relation between the work done by a net force (F) on a particle of mass (m) and the expression 1/2 * m * v^2. How is this expression related to the work (W) the object could do?

Identify the useful, given information.

* This example is not asking for a numerical answer, but rather an equation for an answer. A force F acts on the object with mass m and linear translational velocity v. No other force acts; F is the net force.

Use a kinematic equation to show the relationship between distance, velocity, and acceleration.

```
Vi is initial velocity
Vf is final velocity
a is acceleration
d is the distance of motion
Vf^2 - Vi^2 = 2 * a * d
Rearrange the equation to solve for ad.
a * d = (Vf^2 - Vi^2) / 2
Multiply both sides by the mass (m).
m * a * d = m / 2 * (Vf^2 - Vi^2)
```

Apply Newton’s second law.

```
m * a * d = m / 2 * (Vf^2 - Vi^2)

The force on the object is F = ma,
so you can substitute F for ma.

F * d = m / 2 * (Vf^2 - Vi^2)

The work (W) that the force does is Fd.

W = 1/2 * m * Vf^2 - 1/2 * m * Vi^2

This is the work-energy theorem.

W = (1/2 * m) * (Vf^2 - Vi^2)

```

---

![image_2](3%20-%20Energy/3-02%20-%20Kinetic%20and%20Potential%20Energy/image_2.jpg)

---
3. Find the force needed to bring a 1,325 kg car moving at 27 m/s (about 60 miles per hour) to a stop in a distance of 100.0 m.

Identify the useful information.

```js
let m = 1325; // kg
let v = 27; // m/s
let d = 100.0; // m
```

* Since the work done is equal to the kinetic energy change. find the change in kinetic energy, then use W = F * d to find the net force.

Find the change in kinetic energy.

```js
// Find the initial kinetic energy.
let m = 1325; // kg
let v = 27; // m/s
let Ki = 1/2 * m * Math.pow(v, 2); // J
console.log('Ki =', Ki, 'J');
// Ki = 482962.5 J
console.log('Ki =', Ki.toPrecision(2), 'J');
// Ki = 4.8e+5 J
let Kf = 0; // J
DK = Kf - Ki; //J
console.log('DK =', DK, 'J');
// DK = -482962.5 J
console.log('DK =', DK.toPrecision(2), 'J');
// DK = -4.8e+5 J
```

Find the work done.

```js
// F * d = W
// F = W / d
let m = 1325; // kg
let v = 27; // m/s
let Ki = 1/2 * m * Math.pow(v, 2); // J
let Kf = 0; // J
DK = Kf - Ki; //J
let d = 100.0; // m
let F = DK.toPrecision(2) / d; // N
console.log('F =', F, 'N');
// F = -4800 N

```

Analyze the answer.

* The negative sign results from having assumed the velocity to be positive, so the force stopping the car, which acts in the opposite direction, is negative.

* Although the signs were kept in this solved problem, you could have solved the problem by merely dealing with the magnitudes alone.

---

4. The compressed spring in the spring-powered rifle was found in an earlier problem to have elastic potential energy 1/2 * k * x^2 J = 4.6 J How fast will a 35.0 g projectile move after being fired from the rifle, neglecting friction?

Identify the useful information.

```js
let W = 4.6; // J
let m = 35.0; // g
m = m / 1000; // kg
```

Develop a problem-solving strategy.

* The spring does an amount of work on the projectile equal to its potential energy, which according to the work-energy theorem is then the change in kinetic energy gained by the projectile.

* The initial velocity of the projectile is zero, so the initial K is zero. Knowing that the final K = 1/2 * m * v^2, and that the mass of the projectile is 35.0 g, you can find v^2 and therefore v.

Formulas

```
Vi = 0 m/s
DK = 1/2 * k * x^2 - Vi
v^2 = 2 * K / m
```

Calculate the velocity of the projectile.

```js
let W = 4.6; // J
let m = 35.0; // g
m = m / 1000; // kg
let v = Math.sqrt(2 * W / m); // K
console.log('v =', v, 'm/s');
// v = 16.21286966755555 m/s
console.log('v =', v.toPrecision(2), 'm/s');
// v = 16 m/s
```

---

![image_3](3%20-%20Energy/3-02%20-%20Kinetic%20and%20Potential%20Energy/image_3.jpg)

---

5. A group of physics students conducted an experiment in which they rolled a 0.50 kg toy car down a ramp and onto a table. Along the table they marked off distance intervals of 0.20 m. They measured the time for the car to pass each mark. Track Distance = 1 m

Calculate the potential energy of the toy car when it is launched from a height of 0.25 m.

```js
let m = 0.50; // kg
let g = 9.8; // m/s^2
let h = 0.25; // m
let Ug = m * g * h; // J
console.log('Ug =', Ug, 'J');
// Ug = 1.225 J
console.log('Ug =', Ug.toPrecision(2), 'J');
// Ug = 1.2 J
```

After being launched from the 0.25 m height, it takes the car 0.45 seconds to travel the total 1.00 m distance of the flat section of the track. What is the kinetic energy of the car?

```js
let d = 1.00; // m
let t = 0.45; // s
let v = d / t
console.log('v =', v, 'm/s');
// v = 2.2222222222222223 m/s
let K = 1/2 * m * Math.pow(v, 2); // J
console.log('K =', K, 'J');
// K = 1.234567901234568 J
console.log('K =', K.toPrecision(2), 'J');
// K = 1.2 J
```

Compare the potential energy of the toy car at launch and the kinetic energy of the toy car on the flat surface of the track.

* The potential energy of the car at launch is equal to the kinetic energy of the car on the flat section of the track.

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 47

---

### 3.03 Conservation of Energy 1

![image_1](3%20-%20Energy/3-03%20-%20Conservation%20of%20Energy%201/image_1.jpg)

---

1. A 1,200 kg car is moving at 20.0 m/s, when the driver applies the brakes and brings the car to a stop.How much thermal energy is produced as a result of the friction from the brakes bringing the car to a stop?

Identify the useful information.

```js
let m = 1200; // kg
let v = 20.0; // m/s
```

Calculate the initial kinetic energy.

```js
// K = 1/2 * m * v^2
let m = 1200; // kg
let v = 20.0; // m/s
let K = 1/2 * m * Math.pow(v, 2); // J
console.log('K =', K, 'J');
// K = 240000 J
console.log('K =', K.toPrecision(2), 'J');
// K = 2.4e+5 J
```

Express your answer.

* At the end, all the initial kinetic energy has been converted into thermal energy. So the amount of thermal energy is 2.4 × 10^5 J.

---

2. A 70.0 kg pole vaulter can sprint at the very impressive speed of 9.1 m/s. Use the law of conservation of energy to estimate the height that the pole vaulter can reach.

Identify the useful information.

```js
let m = 70.0; // kg
let v = 9.1; // m/s
```

Apply the law of conservation of energy.

```js
// initial energy = final energy
// 1/2 * m * v^2 = m * g * h^2
// 1/2 * v^2 = g * h^2
// v^2 = 2 * g * h
// h = v^2 / (2 * g)
let v = 9.1; // m/s
let g = 9.8; // m/s^2
let h = Math.pow(v, 2) / 2 / g; // m
console.log('h =', h, 'm');
// h = 4.224999999999999 m
console.log('h =', h.toPrecision(2), 'm');
// h = 4.2 m
```

Analyze your answer.

* Additional effects also help the pole vaulter, so this ismerely a rough estimate.

* Note that the answer does not depend on the mass of the pole vaulter.

---

3. If a rock in free fall reaches the ground moving at 24.0 m/s, how fast is it moving when it has fallen through half its initial height? How would air resistance affect that result?

Identify the useful information.

```js
let v = 24.0; // m/s
```

Apply the law of conservation of energy.

```js
// 1/2 * m * v^2 = m * g * h^2
// 1/2 * v^2 = g * h^2
// h = v^2 / (2 * g)
let g = -9.8; // m/s^2
let v = 24.0; // m/s
let h = Math.pow(v, 2) / 2 / g; // m
console.log('h =', h, 'm');
// h = -29.387755102040813 m
console.log('h =', h.toPrecision(3), 'm');
// h = -29.4 m
```

Find the velocity at half the height.

```js
// 1/2 * m * v^2 = m * g * h^2
// 1/2 * v^2 = g * h^2
// v^2 = 2 * g * h
let g = -9.8; // m/s^2
let v = 24.0; // m/s
let h = Math.pow(v, 2) / 2 / g; // m
let Hhalf = h/2; // m
console.log('Hhalf =', Hhalf, 'm');
// Hhalf = -14.693877551020407 m
let Vhalf = Math.sqrt(2 * g * Hhalf); // m/s
console.log('Vhalf =', Vhalf, 'm/s');
// Vhalf = 16.97056274847714 m/s
console.log('Vhalf =', Vhalf.toPrecision(3), 'm');
// Vhalf = 17.0 m
```

Answer the question completely.

* As might be expected, the final speed does not depend on mass.

* Friction, in the form of air resistance, would transform some ofthe kinetic energy to thermal energy, so that the speed of the fall would be reduced at all heights.

---

4. A pendulum with a mass m = 0.55 kg and length L = 1.2 m is released at an angle of θ=30 degrees. How fast is the pendulum bob moving at θ=15?

Identify the useful information.

```js
let m = 0.55; // kg
let L = 1.2; // m
let degrees = 30; // degrees
let radians = degrees / 180 * Math.PI; // radians
// v = ? when theta = 15 degrees
```

* Note: The height of the bob when the angle is 15 degrees is not half the height when it is at 30 degrees. The challenging part of the problem is to find the height and then the energies.

Determine how far the bob "fell."

* The height of the bob at any given angle will be cosine of theta, so the height at 30 degrees can be found:

```js
// H30 = L * cos (theta)
let theta30 = 30 / 180 * Math.PI; // radians
let L = 1.2; // m
let H30 = L * Math.cos(theta30);
console.log('H30 =', H30, 'm');
// H30 = 1.0392304845413265 m
console.log('H30 =', H30.toPrecision(3), 'm');
// H30 = 1.04 m
let theta15 = 15 / 180 * Math.PI; // radians
let H15 = L * Math.cos(theta15);
console.log('H15 =', H15, 'm');
// H15 = 1.159110991546882 m
console.log('H15 =', H15.toPrecision(3), 'm');
// H15 = 1.16 m
let Dh = H15 - H30; // m
console.log('Dh =', Dh.toPrecision(2), 'm');
// Dh = 0.12 m
```

* The difference beiween the two values is how far the bob "fell": 1.16 m − 1.04 m = 0.12 m

Calculate the loss in potential energy.

* The loss in potential energy will be the same as the gain in kinetic energy.

```js
//U = m * g * h
let m = 0.55; // kg
let L = 1.2; // m
let g = -9.8; // m/s^2
let theta30 = 30 / 180 * Math.PI; // radians
let H30 = L * Math.cos(theta30);
let theta15 = 15 / 180 * Math.PI; // radians
let H15 = L * Math.cos(theta15);
let Dh = H30 - H15; // m
let U = m * g * Dh; // J
console.log('U =', U, 'J');
// U = 0.6461559327599443 J
console.log('U =', U.toPrecision(2), 'J');
// U = 0.65 J
```

* The gain in kinetic energy is 0.65 J.

Calculate the velocity.

```js
// K = 1/2 * m * v^2
let m = 0.55; // kg
let L = 1.2; // m
let g = -9.8; // m/s^2
let theta30 = 30 / 180 * Math.PI; // radians
let H30 = L * Math.cos(theta30);
let theta15 = 15 / 180 * Math.PI; // radians
let H15 = L * Math.cos(theta15);
let Dh = H30 - H15; // m
let U = m * g * Dh; // J
// v = Math.sqrt(2 * K / m)
let v = Math.sqrt(2 * U / m); // m/s
console.log('v =', v, 'm/s');
// v = 1.5328593990672754 m/s
console.log('v =', v.toPrecision(2), 'm/s');
// v = 1.5 m/s
```

* As with many solutions, this is one of several different ways to solve this problem. All valid solutions will give the correct result that matches with observation.

---

![image_2](3%20-%20Energy/3-03%20-%20Conservation%20of%20Energy%201/image_2.jpg)

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 48

---

### 3.04: Conservation of Energy 2

![image_1](3%20-%20Energy/3-04%20-%20Conservation%20of%20Energy%202/image_1.jpg)

---

1. A 0.145 kg baseball is thrown downward at 15.0 m/s from the Leaning Tower of Pisa, from a height of 56 m. How fast would the ball be moving when it reaches the ground if air resistance can be ignored?

Identify the useful information.

```js
let Iv = -15.0; // m/s
let h = -56; // m
```

* The change in kinetic energy will equal the loss of potential energy.

Apply the law of conservation of energy.

```js
// 1/2 * m * Vf^2 - 1/2 * m * Iv^2 = m * g * h
// 1/2 * Vf^2 - 1/2 * Vi = g * h
// Vf^2 = 2 * g * h + Vi^2
// Vf = Math.sqrt(2 * g * h + Vi^2)
let Iv = -15.0; // m/s
let h = -56; // m
let g = -9.8; // m/s^2
let Vf = Math.sqrt(2 * g * h + Math.pow(Iv, 2))
console.log('Vf =', Vf, 'm/s');
// Vf = 36.367567969277246 m/s
console.log('Vf =', Vf.toPrecision(2), 'm/s');
// Vf = 36 m/s
```

Analyze the result.

* This is a high rate of speed. Air resistance, which is a form of friction, would transform some of the kinetic energy to thermal energy and reduce how fast the baseball is moving when it strikes the ground.

---

2. A roller-coaster car starts at rest at a height of 90.0 m at Point A and is moving at a speed of 20.0 m/s up a later incline at Point C. Assuming friction does not affect the motion of the car, what is its height at Point C? Vc = 20.0 m/s.

Identify the useful information.

```js
let v = 20.0; // m/s
// h = ?
```

* The gain in kinetic energy will equal the loss of potential energy.

Apply the law of conservation of energy.

```js
// 1/2 * m * v * c^2 = m * g(Ha - Hc)
// (Ha - Hc) = Vc^2 / (2 * g)
let v = 20.0; // m/s
let g = -9.8; // m/s^2
let Dh = Math.pow(v, 2) / (2 * g); // m
console.log('Dh =', Dh, 'm');
// Dh = -20.408163265306122 m
console.log('Dh =', Dh.toPrecision(3), 'm');
// Dh = -20.4 m
```

Determine the height of Point C.

```js
// (Ha - Hc) = 20.4
let v = 20.0; // m/s
let g = -9.8; // m/s^2
let Dh = Math.pow(v, 2) / (2 * g); // m
let Ha = 90.0; // m
let Hc = Ha - Math.abs(Dh); // m
console.log('Hc =', Hc, 'm');
// Hc = 69.59183673469389 m
console.log('Hc =', Hc.toPrecision(3), 'm');
// Hc = 69.6 m
```

---

3. Suppose that a 40.0 kg crate slides down an 8.2 m ramp at an angle of 15 degrees and with a 12 N force of kinetic friction.How fast is it moving when it reaches the bottom?

Identify the useful information.

```js
let m = 40.0; // kg
let I = 8.2; // m
let theta = 15 / 180 * Math.PI; // radians
let F = -12; // N
```

Find the initial energy.

```js
let m = 40.0; // kg
let I = 8.2; // m
let theta = 15 / 180 * Math.PI; // radians
let Hi = I * Math.sin(theta); // m
console.log('Hi =', Hi, 'm');
// Hi = 2.12231616984067 m
console.log('Hi =', Hi.toPrecision(4), 'm');
// Hi = 2.122 m
let g = 9.8; // m/s^2
let Ei = m * g * Hi.toPrecision(4); // J
console.log('Ei =', Ei, 'J');
// Ei = 831.824 J
console.log('Ei =', Ei.toPrecision(4), 'J');
// Ei = 831.8 J
```

Find the final energy.

```js
// Ef = Ei + Wfr
// Ef = Ei + Ffr * d
let m = 40.0; // kg
let I = 8.2; // m
let theta = 15 / 180 * Math.PI; // radians
let F = -12; // N
let Hi = I * Math.sin(theta); // m
let g = 9.8; // m/s^2
let Ei = m * g * Hi.toPrecision(4); // J
let Ef = Ei + F * I; // J
console.log('Ef =', Ef, 'J');
// Ef = 733.424 J
console.log('Ef =', Ef.toPrecision(4), 'J');
// Ef = 733.4 J
```

---

4. A ball is dropped from a height of 1.0 m onto a hard concrete floor. It bounces back to a height of 0.75 m. Find what fraction of its mechanical energy was lost in the bounce.

Identify the useful information.

```js
let Hi = 1.0; // m
let Hf = 0.75; // ms
```

Calculate the initial and final energies.

* The energy when released and when at greatest height at the end were all potential energy.

```js
// Ei = m * g * Hi
// Ef = m * g * Hf
// ratio = Ef / Ei
let Hi = 1.0; // m
let Hf = 0.75; // ms
// ratio = (m * g * Hf) / (m * g * Hi)
let ratio = Hf / Hi;
console.log('ratio =', ratio);
// ratio = 0.75
```

Analyze the result.

* The ball, if it rises to only 75 percent of its original height on the first bounce, keeps only 75 percent of its initial mechanical energy, and therefore loses 25 percent on each bounce.

---

![image_2](3%20-%20Energy/3-04%20-%20Conservation%20of%20Energy%202/image_2.jpg)

---

5. Use the values from your trials to calculate the percent energy lost on the bounce.

![image_3](3%20-%20Energy/3-04%20-%20Conservation%20of%20Energy%202/image_3.png)

![image_4](3%20-%20Energy/3-04%20-%20Conservation%20of%20Energy%202/image_4.png)

![image_5](3%20-%20Energy/3-04%20-%20Conservation%20of%20Energy%202/image_5.png)

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 49

---

### 3.07 Energy During Collisions

![image_1](3%20-%20Energy/3-07%20-%20Energy%20During%20Collisions/image_1.jpg)

---

1. An air-track glider with mass 0.200 kg moving at 1.0 m/s bumps into a stationary glider of mass 0.300 kg, and then moves with a velocity of −0.200 m/s, while the other glider moves with velocity 0.800 m/s. Determine whether this collision conserved momentum and kinetic energy.

Identify the useful information.

* The initial and final velocities and the two masses are given, so the initial and final total momentum and total kinetic energy can be calculated. Label the first glider "A" and the second glider "B".

```js
let Ma = 0.200; // kg
let iVa = 1.0; // m/s
let Mb  = 0.300; // kg
let iVb = 0; // m/s
let fVa = -0.200; // m/s
let fVb = 0.800; // m/s
```

Calculate the initial and final momentum.

```js
// given
let Ma = 0.200; // kg
let iVa = 1.0; // m/s
let Mb  = 0.300; // kg
let iVb = 0; // m/s
let fVa = -0.200; // m/s
let fVb = 0.800; // m/s

// Initial momentum
let Pi = Ma * iVa + Mb * iVb; // kg * m/s
console.log('Pi =', Pi, 'kg * m/s');
// Pi = 0.2 kg * m/s
console.log('Pi =', Pi.toPrecision(3), 'kg * m/s');
// Pi = 0.200 kg * m/s

// Final momentum
let Pf = Ma * fVa + Mb * fVb;
console.log('Pf =', Pf, 'kg * m/s');
// Pf = 0.19999999999999998 kg * m/s
console.log('Pf =', Pf.toPrecision(3), 'kg * m/s');
// Pf = 0.200 kg * m/s
```

Calculate the initial and final kinetic energy.

```js
// given
let Ma = 0.200; // kg
let iVa = 1.0; // m/s
let Mb  = 0.300; // kg
let iVb = 0; // m/s
let fVa = -0.200; // m/s
let fVb = 0.800; // m/s

// intial  kinetic  energy
let Ki = 1/2 * Ma * Math.pow(iVa, 2) + 1/2 * Mb * Math.pow(iVb, 2); // J
console.log('Ki =', Ki, 'J');
// Ki = 0.1 J
console.log('Ki =', Ki.toPrecision(3), 'J');
// Ki = 0.100 J


// final  kinetic  energy
let Kf = 1/2 * Ma * Math.pow(fVa, 2) + 1/2 * Mb * Math.pow(fVb, 2); // J
console.log('Kf =', Kf, 'J');
// Kf = 0.10000000000000002 J
console.log('Kf =', Kf.toPrecision(3), 'J');
// Kf = 0.100 J
```

Analyze the results.

* Comparison of initial and final momentum shows that total momentum was conserved, as it always must be in a closed system.

* Comparison of initial and final total kinetic energy shows that kinetic energy was also conserved so this is a completely elastic collision.

* The results are consistent with the requirement that momentum is always conserved, but kinetic energy is sometimes conserved. The collision is elastic, because kinetic energy is conserved.

---

2. An air-track glider with mass 0.200 kg moving at 1.0 m/s bumps into a stationary glider of mass 0.300 kg. The two stick together after the collision. How much kinetic energy is lost?

Identify the useful information.

* The masses and initial and final velocities are given, so the initial and final total momentum and total kinetic energy can be calculated.

```js
let Ma = 0.200; // kg
let iVa = 1.0; // m/s
let Mb = 0.300; // kg
let Vb = 0; // m/s
// fVa = ?
// fVb = ?
// Klost = ?
```

Calculate the initial and final momentum.

```js
// given
let Ma = 0.200; // kg
let iVa = 1.0; // m/s
let Mb = 0.300; // kg
let iVb = 0; // m/s

// Initial momentum
let Pi = Ma * iVa + Mb * iVb; // kg * m/s
console.log('Pi =', Pi, 'kg * m/s');
// Pi = 0.2 kg * m/s
console.log('Pi =', Pi.toPrecision(3), 'kg * m/s');
// Pi = 0.200 kg * m/s

// Final momentum
// Pf = (Ma + Mb) * fV
let Pf = Pi;
let Vfinal = Pf / (Ma + Mb);
console.log('Vfinal =', Vfinal, 'kg * m/s');
// Vfinal = 0.4 kg * m/s
console.log('Vfinal =', Vfinal.toPrecision(3), 'kg * m/s');
// Vfinal = 0.400 kg * m/s
```

Calculate the initial and final kinetic energy.

```js
// given
let Ma = 0.200; // kg
let iVa = 1.0; // m/s
let Mb = 0.300; // kg
let iVb = 0; // m/s

// Initial momentum
let Pi = Ma * iVa + Mb * iVb; // kg * m/s

// Final momentum
let Pf = Pi;
let Vfinal = Pf / (Ma + Mb);

// Initial kinetic energy
let Ki = 1/2 * (Ma * Math.pow(iVa, 2) + Mb * Math.pow(iVb, 2));
console.log('Ki =', Ki, 'J');
// Ki = 0.1 J
console.log('Ki =', Ki.toPrecision(3), 'J');
// Ki = 0.100 J
// Final kinetic energy
let Kf = 1/2 * (Ma + Mb) * Math.pow(Vfinal, 2);
console.log('Kf =', Kf, 'J');
// Kf = 0.04000000000000001 J
console.log('Kf =', Kf.toPrecision(3), 'J');
// Kf = 0.0400 J
// So the kinetic energy changed by
let DK = Math.abs(Kf - Ki);
console.log('DK =', DK, 'J');
// DK = 0.06 J
console.log('DK =', DK.toPrecision(2), 'J');
// DK = 0.060 J
```

Analyze the results.

* Momentum was conserved. Comparison of initial and final total kinetic energy, however, shows that kinetic energy was not conserved in the collision.

---

3. An air-track glider with mass 0.200 kg moving at 1.0 m/s bumps into a stationary glider of mass 0.300 kg, and then moves with a velocity of −0.230 m/s, while the other glider moves with velocity 0.820 m/s. Determine whether this collision conserved momentum and kinetic energy.

Identify the useful information.

* The initial and final velocities and the two masses are given, so the initial and final total momentum and total kinetic energy can be calculated. Label the first glider "A" and the second glider "B".

```js
let Ma = 0.200; // kg
let iVa = 1.0; // m/s
let Mb = 0.300; // kg
let iVb = 0; // m/s
let fVa = -0.230; // m/s
let fVb = 0.820; // m/s
```

Calculate the initial and final momentum.

```js
// given
let Ma = 0.200; // kg
let iVa = 1.0; // m/s
let Mb = 0.300; // kg
let iVb = 0; // m/s
let fVa = -0.230; // m/s
let fVb = 0.820; // m/s

// Initial momentum
let Pi = Ma * iVa + Mb * iVb; // kg * m/s
console.log('Pi =', Pi, 'kg * m/s');
// Pi = 0.2 kg * m/s
console.log('Pi =', Pi.toPrecision(3), 'kg * m/s');
// Pi = 0.200 kg * m/s

// Final momentum
let Pf = Ma * fVa + Mb * fVb;
console.log('Pf =', Pf, 'kg * m/s');
// Pf = 0.19999999999999996 kg * m/s
console.log('Pf =', Pf.toPrecision(3), 'kg * m/s');
// Pf = 0.200 kg * m/s
```

Calculate the initial and final kinetic energy.

```js
// given
let Ma = 0.200; // kg
let iVa = 1.0; // m/s
let Mb = 0.300; // kg
let iVb = 0; // m/s
let fVa = -0.230; // m/s
let fVb = 0.820; // m/s

// intial  kinetic  energy
let Ki = 1/2 * Ma * Math.pow(iVa, 2) + 1/2 * Mb * Math.pow(iVb, 2); // J
console.log('Ki =', Ki, 'J');
// Ki = 0.1 J
console.log('Ki =', Ki.toPrecision(3), 'J');
// Ki = 0.100 J


// final  kinetic  energy
let Kf = 1/2 * Ma * Math.pow(fVa, 2) + 1/2 * Mb * Math.pow(fVb, 2); // J
console.log('Kf =', Kf, 'J');
// Kf = 0.10614999999999998 J
console.log('Kf =', Kf.toPrecision(3), 'J');
// Kf = 0.106 J
```

Analyze the results.

* Comparison of initial and final momentum shows that total momentum was conserved, as it always must be in a closed system.

* Comparison of initial and final total kinetic energy shows that kinetic energy increased in the collision. This can occur only if there is a source of energy, such as the energy stored in a spring.

---

4. A billiard ball of mass 0.16 kg moving at 0.52 m/s collides directly into another stationary billiard ball of the same mass. Find the final velocity of each billiard ball.Assume this is an elastic collision occurring in one dimension.

Identify the useful information.

* The masses and the initial velocities are known, allowing the initial kinetic energy and initial momentum to be calculated. Conservation of momentum and conservation of kinetic energy each give an equation.

* Both equations involving the final velocities must be true at the same time, so you can combine and manipulate the equations to find the values of the final velocities.

```js
let Ma = 0.16; // kg
let iVa = 0.52; // m/s
let Mb = 0.16; // kg
let iVb = 0; // m/s
// fVa = ?
// fVb = ?
```

Solve the momentum and energy equations at the same time.

```js
// given
let Ma = 0.16; // kg
let iVa = 0.52; // m/s
let Mb = 0.16; // kg
let iVb = 0; // m/s

// Initial momentum
// Since B is not moving initially
let Pi = iVa;

// Initial kinetic energy
let Ki = 1/2 * Ma * Math.pow(iVa, 2);
```

* Because of conservation of momentum and kinetic energy, set the initial momentum equal to final momentum and intial kinteric energy to final kinetic energy.

```js
// iVa = fVa + fVb
// Iva^2 = fVa^2 + fVb^2
```

Calculate the velocities.

* The unknown velocities VA,final and VB,final final must
satisfy both equation (1) and (2).

* Square both sides of equation (1):

```js
// iVa^2 = fVa^2 + fVb^2 + 2*fVa*fVb 
```

* Subtract equation (3) from equation (2),  (That is, subtract the right side of (3) from the right side of (2), and similarly for the left sides).

```js
// Obtain:
// -2 * fVa * fVb = 0
// or
// fVa * fVb = 0
```

Analyze the results.

* The only way to multiply two numbers and obtain zero is for one of the numbers to be zero. So one of the two final velocities must be zero.

* If fVa is zero, then all of the final kinetic energy is carried by the second ball, so that its final velocity is VA,initial.

* Otherwise, fVb is zero, then all of the final kinetic energy is carried by the first ball, so that its final velocity is iVa. In this latter case, the initial and final velocities are the same as before the collision, and no collision has occurred.

* For an object in one dimension elastically colliding with another of the same mass initially at rest, either the two objects interchange their velocities, or else no change in velocity—and no collision—occurs.

---

![image_2](3%20-%20Energy/3-07%20-%20Energy%20During%20Collisions/image_2.jpg)

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 50

---

## 4: Thermal Energy

---

### 4.01: Kinetic-Molecular Theory

![image_1](4%20-%20Thermal%20Energy/4-01%20-%20Kinetic-Molecular%20Theory/image_1.png)

![image_2](4%20-%20Thermal%20Energy/4-01%20-%20Kinetic-Molecular%20Theory/image_2.png)

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 51

---

### 4.02: Specific Heat

![image_1](4%20-%20Thermal%20Energy/4-02%20-%20Specific%20Heat/image_1.jpg)

![image_2](4%20-%20Thermal%20Energy/4-02%20-%20Specific%20Heat/image_2.png)

![image_3](4%20-%20Thermal%20Energy/4-02%20-%20Specific%20Heat/image_3.png)

![image_4](4%20-%20Thermal%20Energy/4-02%20-%20Specific%20Heat/image_4.png)

---

1. If 100.0 g of a substance absorbs 1.17 kJ when its temperature increases by 30.0°C, then what is the substance?

Given:

```js
let q = 1170; // J
let m = 100.0; // g
let DT = 30.0; // degrees C
// let C = ?
```

Write the equation for specific heat.

```js
let q = 1170; // J
let m = 100.0; // g
let DT = 30.0; // degrees C
let C = q / m / DT; // J / (g * degrees C)
console.log('C =', C, 'J / (g * degrees C)');
// C = 0.38999999999999996 J / (g * degrees C)
console.log('C =', C.toPrecision(2), 'J / (g * degrees C)');
// C = 0.39 J / (g * degrees C)
```

Look up the specific heat in a table of specific heat values to identify the substance.

```js
let q = 1170; // J
let m = 100.0; // g
let DT = 30.0; // degrees C
let C = q / m / DT; // J / (g * degrees C)
console.log('C =', C.toPrecision(2), 'J / (g * degrees C)');
// C = 0.39 J / (g * degrees C)
let lookup = {
    "2.05": "water (ice)",
    "0.46": "iron",
    "0.9": "aluminum",
    "0.13": "gold",
    "0.39": "copper",
    "4.7": "ammonia (liquid)",
};
console.log('Lookup Table', JSON.stringify(lookup, null, 2));
let strC = C.toPrecision(2);
let substance = lookup[strC];
console.log('The substance for', strC, 'is', substance);
// The substance for 0.39 is copper
```

---

2. Determine how much heat is required to heat a 0.50 kg cast-iron skillet by 200 K, use the specific heat equation.

```js
let m = 0.50; // kg
let DT = 200.0; // K
let C = 450; // J / (kg * K)
let Cfe = C; // C of Iron
let q = m * C * DT; // J
console.log('q =', q, 'J');
// q = 45000 J 
```

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 52

---

### 4.05: States of Matter

![image_1](4%20-%20Thermal%20Energy/4-05%20-%20States%20of%20Matter/image_1.jpg)

![image_2](4%20-%20Thermal%20Energy/4-05%20-%20States%20of%20Matter/image_2.jpg)

![image_3](4%20-%20Thermal%20Energy/4-05%20-%20States%20of%20Matter/image_3.jpg)

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 53

---

### 4.06: Heat During Change of State

![image_1](4%20-%20Thermal%20Energy/4-06%20-%20Heat%20During%20Change%20of%20State/image_1.jpg)

![image_2](4%20-%20Thermal%20Energy/4-06%20-%20Heat%20During%20Change%20of%20State/image_2.png)

![image_3](4%20-%20Thermal%20Energy/4-06%20-%20Heat%20During%20Change%20of%20State/image_3.png)

![image_4](4%20-%20Thermal%20Energy/4-06%20-%20Heat%20During%20Change%20of%20State/image_4.png)

![image_5](4%20-%20Thermal%20Energy/4-06%20-%20Heat%20During%20Change%20of%20State/image_5.png)

![image_6](4%20-%20Thermal%20Energy/4-06%20-%20Heat%20During%20Change%20of%20State/image_6.png)

---

1. What is the total heat required to change ice from –100°C
negative 100 degree C to steam at 200°C? Mass is 100 g.

![image_7](4%20-%20Thermal%20Energy/4-06%20-%20Heat%20During%20Change%20of%20State/image_7.png)

![image_9](4%20-%20Thermal%20Energy/4-06%20-%20Heat%20During%20Change%20of%20State/image_9.png)

Heating ice from –100°C to 0°C

`q = m * C * DT`

```js
let m = 100; // g
let QheatIce = m * 2.05 / 1000 * 100; // kJ
console.log('QheatIce =', QheatIce, 'kJ');
// QheatIce = 20.499999999999996 kJ
console.log('QheatIce =', QheatIce.toPrecision(3), 'kJ');
// QheatIce = 20.5 kJ
```

Ice melting at 0°C

`q = m * DHf`

```js
let m = 100; // g
let QiceMelt = m * 334 / 1000; // kJ
console.log('QiceMelt =', QiceMelt, 'kJ');
// QiceMelt = 33.4 kJ
```

Heating liquid water from 0°C to 100°C

`q = m * C * DT`

```js
let m = 100; // g
let QheatWater = m * 4.18 / 10; // kJ
console.log('QheatWater =', QheatWater, 'kJ');
// QheatWater = 41.8 kJ
```

Liquid water boiling at 100°C

`q = m * DHf`

```js
let m = 100; // g
let QboilWater = m * 2.26; // kJ
console.log('QboilWater =', QboilWater, 'kJ');
// QboilWater = 225.99999999999997 kJ
console.log('QboilWater =', Math.round(QboilWater), 'kJ');
// QboilWater = 226 kJ
```

Heating steam from 100°C to 200°C

`q = m * C * DT`

```js
let m = 100; // g
let QheatSteam = m * 2.08 / 10; // kJ
console.log('QheatSteam =', QheatSteam, 'kJ');
// QheatSteam = 20.8 kJ
```

Total heat required

```js
let q = QheatIce + QiceMelt + QheatWater + QboilWater + QheatSteam;
console.log('q =', q, 'kJ');
// q = 342.49999999999994 kJ
console.log('q =', q.toPrecision(4), 'kJ');
// q = 342.5 kJ
```

---

2. What is the total heat required to change steam at 200°C to ice at –100°C? Mass is 100 g.

![image_8](4%20-%20Thermal%20Energy/4-06%20-%20Heat%20During%20Change%20of%20State/image_8.png)

![image_10](4%20-%20Thermal%20Energy/4-06%20-%20Heat%20During%20Change%20of%20State/image_10.png)

```js
let q = -QheatIce - QiceMelt - QheatWater - QboilWater - QheatSteam;
console.log('q =', q, 'kJ');
// q = -342.49999999999994 kJ
console.log('q =', q.toPrecision(4), 'kJ');
// q = -342.5 kJ
```

---

3. You have a 0.10 kg block of lead. Lead melts at 327.5°C. C = 130 J/(kg⋅°C), and ΔHf for lead = 2.04 × 10^4 J/kg. Let's say you start at room temperature (25°C). How much heat must you transfer to melt all the lead?

Heat lead to its melting point:

`q = m * C * DT`

```js
let m = 0.10; // kg
let C = 130; // J/(kg⋅°C)
let DT = 327.5 - 25; // °C
let QheatSolidLead = m * C * DT;
console.log('QheatSolidLead', QheatSolidLead, 'J');
// QheatSolidLead 3932.5 J
console.log('QheatSolidLead', QheatSolidLead.toPrecision(3), 'J');
// QheatSolidLead 3.93e+3 J
```

Convert solid lead to liquid lead at its melting point:

`q = m * DHf`

```js
let m = 0.10; // kg
let DHf = 2.04 * Math.pow(10, 4); // J/kg
let QconvertLead = m * DHf;
console.log('QconvertLead', QconvertLead, 'J');
// QconvertLead 2040 J
console.log('QconvertLead', QconvertLead.toPrecision(3), 'J');
// QconvertLead 2.04e+3 J
```

Total heat required

```js
let q = Number(QheatSolidLead.toPrecision(3)) + Number(QconvertLead.toPrecision(3));
console.log('q =', q, 'J');
// q = 5972.5 J
console.log('q', q.toPrecision(2), 'J');
// q 6.0e+3 J
```

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 54

---

### 4.07: First Law of Thermodynamics

![image_1](4%20-%20Thermal%20Energy/4-07%20-%20First%20Law%20of%20Thermodynamics/image_1.jpg)

![image_2](4%20-%20Thermal%20Energy/4-07%20-%20First%20Law%20of%20Thermodynamics/image_2.png)

![image_3](4%20-%20Thermal%20Energy/4-07%20-%20First%20Law%20of%20Thermodynamics/image_3.png)

![image_4](4%20-%20Thermal%20Energy/4-07%20-%20First%20Law%20of%20Thermodynamics/image_4.png)

![image_5](4%20-%20Thermal%20Energy/4-07%20-%20First%20Law%20of%20Thermodynamics/image_5.png)

---

1. A total of 135 J of work is done by a gas refrigerant as it expands. The total heat transferred to the refrigerant is 21 J. What is the change in energy of the system?

What do you know, and what are you trying to find?

```js
// Given
let W = 135; // J (W is done by the system, so W > 0)
let Q = 21; // J (W is transferred by the system, so W > 0)
// Unknown
//let DU = ?
```

Write the equation (rearrange if necessary).

`DU = Q - W`

Solve for the unknown.

```js
let W = 135; // J (W is done by the system, so W > 0)
let Q = 21; // J (W is transferred by the system, so W > 0)
let DU = Q - W;
console.log('DU =', DU, 'J');
// DU = -114 J
```

---

2. How much work can be extracted from 1.0 × 103 J of heat when the hot and cold reservoirs are 373 K and 273 K, respectively?

What do you know, and what are you trying to find?

```js
// Given:
let QH = 1.0 * Math.pow(10, 3); // J
let TH = 373; // K
let TL = 273; // K
// Unknown:
// let W = ?
```

What equations will you need to find the unknown? Rearrange them if necessary.

`QL / QH = TL / TH`

`QL = QH * TL / TH`

`QH = W + QL`

`W = QH - QL`

Solve for the unknown.

```js
let QH = 1.0 * Math.pow(10, 3); // J
let TH = 373; // K
let TL = 273; // K
let QL = QH * TL / TH; // J
console.log('QL =', QL, 'J');
// QL = 731.9034852546916 J
let W = QH - QL;
console.log('W =', W, 'J');
// W = 268.09651474530835 J
console.log('W =', W.toPrecision(2), 'J');
// W = 2.7e+2 J
```

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 55

---

### 4.08: Second Law of Thermodynamics and Entropy

---

![image_1](4%20-%20Thermal%20Energy/4-08%20-%20Second%20Law%20of%20Thermodynamics%20and%20Entropy/image_1.jpg)

![image_2](4%20-%20Thermal%20Energy/4-08%20-%20Second%20Law%20of%20Thermodynamics%20and%20Entropy/image_2.png)

![image_3](4%20-%20Thermal%20Energy/4-08%20-%20Second%20Law%20of%20Thermodynamics%20and%20Entropy/image_3.png)

![image_4](4%20-%20Thermal%20Energy/4-08%20-%20Second%20Law%20of%20Thermodynamics%20and%20Entropy/image_4.png)

![image_5](4%20-%20Thermal%20Energy/4-08%20-%20Second%20Law%20of%20Thermodynamics%20and%20Entropy/image_5.png)

![image_6](4%20-%20Thermal%20Energy/4-08%20-%20Second%20Law%20of%20Thermodynamics%20and%20Entropy/image_6.png)

![image_7](4%20-%20Thermal%20Energy/4-08%20-%20Second%20Law%20of%20Thermodynamics%20and%20Entropy/image_7.png)

![image_8](4%20-%20Thermal%20Energy/4-08%20-%20Second%20Law%20of%20Thermodynamics%20and%20Entropy/image_8.png)

![image_9](4%20-%20Thermal%20Energy/4-08%20-%20Second%20Law%20of%20Thermodynamics%20and%20Entropy/image_9.png)

![image_10](4%20-%20Thermal%20Energy/4-08%20-%20Second%20Law%20of%20Thermodynamics%20and%20Entropy/image_10.png)

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 56

---

## 5 - Waves

---

### 5.01: Characteristics of Waves 1

---

![image_1](5%20-%20Waves/5-01%20-%20Characteristics%20of%20Waves%201/image_1.jpg)

![image_2](5%20-%20Waves/5-01%20-%20Characteristics%20of%20Waves%201/image_2.png)

![image_3](5%20-%20Waves/5-01%20-%20Characteristics%20of%20Waves%201/image_3.png)

![image_4](5%20-%20Waves/5-01%20-%20Characteristics%20of%20Waves%201/image_4.png)

![image_5](5%20-%20Waves/5-01%20-%20Characteristics%20of%20Waves%201/image_5.png)

![image_6](5%20-%20Waves/5-01%20-%20Characteristics%20of%20Waves%201/image_6.png)

* In a longitudinal wave, particles move back and forth in a path that is parallel to the direction of the wave's motion.

* In a transverse wave, particles move in a path that is perpendicular to the direction of the wave's motion.

* In a surface wave, particles move in a circular path that is both parallel and perpendicular to the direction of the wave's motion.

![image_7](5%20-%20Waves/5-01%20-%20Characteristics%20of%20Waves%201/image_7.png)

![image_8](5%20-%20Waves/5-01%20-%20Characteristics%20of%20Waves%201/image_8.png)

![image_9](5%20-%20Waves/5-01%20-%20Characteristics%20of%20Waves%201/image_9.png)

![image_10](5%20-%20Waves/5-01%20-%20Characteristics%20of%20Waves%201/image_10.png)

![image_11](5%20-%20Waves/5-01%20-%20Characteristics%20of%20Waves%201/image_11.png)

![image_12](5%20-%20Waves/5-01%20-%20Characteristics%20of%20Waves%201/image_12.png)

![image_13](5%20-%20Waves/5-01%20-%20Characteristics%20of%20Waves%201/image_13.png)

![image_14](5%20-%20Waves/5-01%20-%20Characteristics%20of%20Waves%201/image_14.png)

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 57

---

### 5.02: Characteristics of Waves 2

---

![image_1](5%20-%20Waves/5-02%20-%20Characteristics%20of%20Waves%202/image_1.jpg)

![image_2](5%20-%20Waves/5-02%20-%20Characteristics%20of%20Waves%202/image_2.png)

![image_3](5%20-%20Waves/5-02%20-%20Characteristics%20of%20Waves%202/image_3.png)

![image_4](5%20-%20Waves/5-02%20-%20Characteristics%20of%20Waves%202/image_4.png)

![image_5](5%20-%20Waves/5-02%20-%20Characteristics%20of%20Waves%202/image_5.png)

![image_6](5%20-%20Waves/5-02%20-%20Characteristics%20of%20Waves%202/image_6.png)

![image_7](5%20-%20Waves/5-02%20-%20Characteristics%20of%20Waves%202/image_7.png)

![image_8](5%20-%20Waves/5-02%20-%20Characteristics%20of%20Waves%202/image_8.png)

![image_9](5%20-%20Waves/5-02%20-%20Characteristics%20of%20Waves%202/image_9.png)

![image_10](5%20-%20Waves/5-02%20-%20Characteristics%20of%20Waves%202/image_10.png)

![image_11](5%20-%20Waves/5-02%20-%20Characteristics%20of%20Waves%202/image_11.png)

![image_12](5%20-%20Waves/5-02%20-%20Characteristics%20of%20Waves%202/image_12.png)

![image_13](5%20-%20Waves/5-02%20-%20Characteristics%20of%20Waves%202/image_13.png)

![image_14](5%20-%20Waves/5-02%20-%20Characteristics%20of%20Waves%202/image_14.png)

![image_15](5%20-%20Waves/5-02%20-%20Characteristics%20of%20Waves%202/image_15.png)

---

1. A wave with a period of 0.5 s has a frequency of 2 Hz:

```js
let T = 0.5; // s
let f = 1 / T; // Hz
console.log('f =', f, 'Hz');
// f = 2 Hz
```

---

2. What is the frequency of a wave with a period of 0.1 s?

```js
let T = 0.1; // s
let f = 1 / T; // Hz
console.log('f =', f, 'Hz');
// f = 10 Hz
```

---

3. How fast does a wave with a λ = 3.0 m and a period of T = 0.3 s travel?

```js
let wavelength = 3.0; // m
let T = 0.3; // s
let v = wavelength / T; // m/s
console.log('v =', v, 'm/s');
// v = 10 m/s
```

---

4. How fast does a wave with a λ = 3.0 m if the frequency is 3.33 Hz?

```js
let wavelength = 3.0; // m
let f = 3.3; // Hz
let v = wavelength * f; // m/s
console.log('v =', v, 'm/s');
// v = 9.899999999999999 m/s
console.log('v =', v.toPrecision(2), 'm/s');
// v = 9.9 m/s
console.log('v =', Math.round(v), 'm/s');
// v = 10 m/s
```

---

5. Five waves pass a dock in 10.0 s. If the waves are traveling at 10.0 m/s, then what is their wavelength?

```js
let v = 10.0; // m/s
let number_of_waves = 5;
let T = 10.0; // s
let f =  number_of_waves / T; // Hz
console.log('f =', f, 'Hz');
// f = 0.5 Hz
let wavelength = v / f; // m
console.log('wavelength =', wavelength, 'm');
// wavelength = 20 m
```

---

6. What is the wavelength of waves with a period of 0.5 s traveling at 20 m/s?

```js
let T = 0.5; // s
let v = 20; // m/s
let wavelength = v * T; // m
console.log('wavelength =', wavelength, 'm');
// wavelength = 10 m
```

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 58

---

### 5.03: Sound: Vibration and Waves

---

![image_1](5%20-%20Waves/5-03%20-%20Sound%20Vibration%20and%20Waves/image_1.png)

![image_2](5%20-%20Waves/5-03%20-%20Sound%20Vibration%20and%20Waves/image_2.png)

![image_3](5%20-%20Waves/5-03%20-%20Sound%20Vibration%20and%20Waves/image_3.png)

![image_4](5%20-%20Waves/5-03%20-%20Sound%20Vibration%20and%20Waves/image_4.png)

![image_5](5%20-%20Waves/5-03%20-%20Sound%20Vibration%20and%20Waves/image_5.png)

![image_6](5%20-%20Waves/5-03%20-%20Sound%20Vibration%20and%20Waves/image_6.png)

![image_7](5%20-%20Waves/5-03%20-%20Sound%20Vibration%20and%20Waves/image_7.png)

* Sound and Sound Waves: Use the terms sound waves and sound with care. A sound wave is the way in which the energy of a mechanically vibrating object is transmitted through a medium. People talk of the "speed of sound" but what they mean is the "speed of a sound wave." Sound is what we hear. The ringing of a bell is a sound; the motion of the bell comes to our ears via a sound wave.

![image_8](5%20-%20Waves/5-03%20-%20Sound%20Vibration%20and%20Waves/image_8.jpg)

![image_9](5%20-%20Waves/5-03%20-%20Sound%20Vibration%20and%20Waves/image_9.png)

![image_10](5%20-%20Waves/5-03%20-%20Sound%20Vibration%20and%20Waves/image_10.png)

![image_11](5%20-%20Waves/5-03%20-%20Sound%20Vibration%20and%20Waves/image_11.png)

![image_12](5%20-%20Waves/5-03%20-%20Sound%20Vibration%20and%20Waves/image_12.png)

![image_13](5%20-%20Waves/5-03%20-%20Sound%20Vibration%20and%20Waves/image_13.png)

![image_14](5%20-%20Waves/5-03%20-%20Sound%20Vibration%20and%20Waves/image_14.png)

![image_15](5%20-%20Waves/5-03%20-%20Sound%20Vibration%20and%20Waves/image_15.png)

![image_16](5%20-%20Waves/5-03%20-%20Sound%20Vibration%20and%20Waves/image_16.png)

![image_17](5%20-%20Waves/5-03%20-%20Sound%20Vibration%20and%20Waves/image_17.png)

---

1. How fast is the speed of sound waves in air at 15°C?

```js
let medium_air_0C = 331; // m/s
let T = 15; // °C
let v = (medium_air_0C + 0.60 * T); // m/s
console.log('v =', v, 'm/s');
// v = 340 m/s
```

---

2. How far does a sound wave travel through air at 20°C in 5.00 s?

```js
let medium_air_20C = 343; // m/s
let v = medium_air_20C; // m/s
let t = 5.00; // s
let d = v * t; // m
console.log('d =', d, 'm');
// d = 1715 m
console.log('d =', d / 1000, 'km');
// d = 1.715 km
console.log('d =', (d / 1000).toPrecision(3), 'km');
// d = 1.72 km
```

---

3. You shout across a canyon through air at 20°C and hear an echo 5.00 s later. How wide is the canyon?

```js
let t = 2.50; // s
let T = 20; // °C
let medium_air_20C = 343; // m/s
let v = medium_air_20C; // m/s
let d = v * t; // m
console.log('d =', d, 'm');
// d = 857.5 m
console.log('d =', d / 1000, 'km');
// d = 0.8575 km
console.log('d =', (d / 1000).toPrecision(3), 'km');
// d = 0.858 km
```

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 59

---

### 5.04: Qualities of Sound

---

![image_1](5%20-%20Waves/5-04%20-%20Qualities%20of%20Sound/image_1.png)

![image_2](5%20-%20Waves/5-04%20-%20Qualities%20of%20Sound/image_2.jpg)

![image_3](5%20-%20Waves/5-04%20-%20Qualities%20of%20Sound/image_3.png)

![image_4](5%20-%20Waves/5-04%20-%20Qualities%20of%20Sound/image_4.png)

![image_5](5%20-%20Waves/5-04%20-%20Qualities%20of%20Sound/image_5.png)

![image_6](5%20-%20Waves/5-04%20-%20Qualities%20of%20Sound/image_6.jpg)

![image_7](5%20-%20Waves/5-04%20-%20Qualities%20of%20Sound/image_7.jpg)

![image_8](5%20-%20Waves/5-04%20-%20Qualities%20of%20Sound/image_8.png)

![image_9](5%20-%20Waves/5-04%20-%20Qualities%20of%20Sound/image_9.png)

![image_10](5%20-%20Waves/5-04%20-%20Qualities%20of%20Sound/image_10.png)

![image_11](5%20-%20Waves/5-04%20-%20Qualities%20of%20Sound/image_11.jpg)

![image_12](5%20-%20Waves/5-04%20-%20Qualities%20of%20Sound/image_12.png)

![image_13](5%20-%20Waves/5-04%20-%20Qualities%20of%20Sound/image_13.jpg)

![image_14](5%20-%20Waves/5-04%20-%20Qualities%20of%20Sound/image_14.png)

![image_15](5%20-%20Waves/5-04%20-%20Qualities%20of%20Sound/image_15.png)

![image_16](5%20-%20Waves/5-04%20-%20Qualities%20of%20Sound/image_16.png)

![image_17](5%20-%20Waves/5-04%20-%20Qualities%20of%20Sound/image_17.png)

![image_18](5%20-%20Waves/5-04%20-%20Qualities%20of%20Sound/image_18.png)

![image_19](5%20-%20Waves/5-04%20-%20Qualities%20of%20Sound/image_19.png)

![image_20](5%20-%20Waves/5-04%20-%20Qualities%20of%20Sound/image_20.png)

![image_21](5%20-%20Waves/5-04%20-%20Qualities%20of%20Sound/image_21.png)

![image_22](5%20-%20Waves/5-04%20-%20Qualities%20of%20Sound/image_22.png)

![image_23](5%20-%20Waves/5-04%20-%20Qualities%20of%20Sound/image_23.png)

![image_24](5%20-%20Waves/5-04%20-%20Qualities%20of%20Sound/image_24.png)

* Doppler effect - the change in the observed frequency of a wave because of the motion of the source or the observer toward or away from the other; the frequency increases when the source and observer approach each other and decreases when they move apart

![image_25](5%20-%20Waves/5-04%20-%20Qualities%20of%20Sound/image_25.png)

![image_26](5%20-%20Waves/5-04%20-%20Qualities%20of%20Sound/image_26.png)

---

1. What is the dB loudness for a pressure of 2 × 10^-5 N/m^2?

```js
function calculateDb(pressure) {
  // Reference pressure for dB calculation (20 micropascals)
  let referencePressure = 2 * Math.pow(10, -5); // dB

  // Calculate the ratio of the two pressures
  let pressureRatio = pressure / referencePressure;

  // Calculate the decibel value using the logarithmic formula
  let loudness = 20 * Math.log10(pressureRatio);

  return loudness;
}
let pressure = 2 * Math.pow(10, -5); // N/m^2
let loudness = calculateDb(pressure); // dB
console.log('loudness =', loudness, 'dB');
// loudness = 0 dB
```

---

2. What is the dB loudness for a pressure of 2 × 10^-4 N/m^2?

```js
function calculateDb(pressure) {
  // Reference pressure for dB calculation (20 micropascals)
  let referencePressure = 2 * Math.pow(10, -5); // dB

  // Calculate the ratio of the two pressures
  let pressureRatio = pressure / referencePressure;

  // Calculate the decibel value using the logarithmic formula
  let loudness = 20 * Math.log10(pressureRatio);

  return loudness;
}
let pressure = 2 * Math.pow(10, -4); // N/m^2
let loudness = calculateDb(pressure); // dB
console.log('loudness =', loudness, 'dB');
// loudness = 20 dB
```

---

3. What is the dB loudness for a pressure of 2 × 10^-3 N/m^2?

```js
function calculateDb(pressure) {
  // Reference pressure for dB calculation (20 micropascals)
  let referencePressure = 2 * Math.pow(10, -5); // dB

  // Calculate the ratio of the two pressures
  let pressureRatio = pressure / referencePressure;

  // Calculate the decibel value using the logarithmic formula
  let loudness = 20 * Math.log10(pressureRatio);

  return loudness;
}
let pressure = 2 * Math.pow(10, -3); // N/m^2
let loudness = calculateDb(pressure); // dB
console.log('loudness =', loudness, 'dB');
// loudness = 40 dB
```

---

4. What is the pressure (N/m^2) for a loudness of 120 dB loudness?

```js
function calculatePressure(loudness) {
  // Reference pressure for dB calculation (20 micropascals)
  let referencePressure = 2 * Math.pow(10, -5);

  // Calculate the pressure ratio using the decibel value
  let pressureRatio = Math.pow(10, loudness / 20);

  // Calculate the pressure by multiplying with the reference pressure
  let pressure = pressureRatio * referencePressure;

  return pressure;
}

let loudness = 120; // dB
let pressure = calculatePressure(loudness);
console.log('pressure =', pressure, 'N/m^2');
// pressure = 20 N/m^2
```

---

5. What is the intensity of the sound at 1.0 m away, if a siren has a power of 2.0 × 10^–5 W at the source?

```js
let P = 2.0 * Math.pow(10, -5); // W
let r = 1.0; // m
let I = P / 4 / Math.PI / Math.pow(r, 2); // W / m^2
console.log('I =', I.toExponential(), 'W / m^2');
// I = 1.5915494309189533e-6 W / m^2
console.log('I =', Number(I.toPrecision(2)).toExponential(), 'W / m^2');
// I = 1.6e-6 W / m^2
```

---

6. What is the intensity of the sound at 2.0 m away, if a siren has a power of 2.0 × 10^–5 W at the source?

```js
let P = 2.0 * Math.pow(10, -5); // W
let r = 2.0; // m
let I = P / 4 / Math.PI / Math.pow(r, 2); // W / m^2
console.log('I =', I.toExponential(), 'W / m^2');
// I = 3.9788735772973833e-7 W / m^2
console.log('I =', Number(I.toPrecision(2)).toExponential(), 'W / m^2');
// I = 4e-7 W / m^2
```

---

7. What is the intensity of the sound at 3.0 m away, if a siren has a power of 2.0 × 10^–5 W at the source?

```js
let P = 2.0 * Math.pow(10, -5); // W
let r = 3.0; // m
let I = P / 4 / Math.PI / Math.pow(r, 2); // W / m^2
console.log('I =', I.toExponential(), 'W / m^2');
// I = 1.768388256576615e-7 W / m^2
console.log('I =', Number(I.toPrecision(2)).toExponential(), 'W / m^2');
// I = 1.8e-7 W / m^2
```

---

8. What is the intensity of the sound at 4.0 m away, if a siren has a power of 2.0 × 10^–5 W at the source?

```js
let P = 2.0 * Math.pow(10, -5); // W
let r = 4.0; // m
let I = P / 4 / Math.PI / Math.pow(r, 2); // W / m^2
console.log('I =', I.toExponential(), 'W / m^2');
// I = 9.947183943243458e-8 W / m^2
console.log('I =', Number(I.toPrecision(2)).toExponential(), 'W / m^2');
// I = 9.9e-8 W / m^2
```

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 60

---

## 6: Light

---

### 6.01: The Electromagnetic Spectrum

---

![image_1](6%20-%20Light/6-01%20-%20The%20Electromagnetic%20Spectrum/image_1.png)

![image_2](6%20-%20Light/6-01%20-%20The%20Electromagnetic%20Spectrum/image_2.png)

![image_3](6%20-%20Light/6-01%20-%20The%20Electromagnetic%20Spectrum/image_3.png)

![image_4](6%20-%20Light/6-01%20-%20The%20Electromagnetic%20Spectrum/image_4.png)

![image_5](6%20-%20Light/6-01%20-%20The%20Electromagnetic%20Spectrum/image_5.png)

![image_6](6%20-%20Light/6-01%20-%20The%20Electromagnetic%20Spectrum/image_6.png)

![image_7](6%20-%20Light/6-01%20-%20The%20Electromagnetic%20Spectrum/image_7.png)

![image_8](6%20-%20Light/6-01%20-%20The%20Electromagnetic%20Spectrum/image_8.png)

![image_9](6%20-%20Light/6-01%20-%20The%20Electromagnetic%20Spectrum/image_9.png)

![image_10](6%20-%20Light/6-01%20-%20The%20Electromagnetic%20Spectrum/image_10.png)

![image_11](6%20-%20Light/6-01%20-%20The%20Electromagnetic%20Spectrum/image_11.png)

![image_12](6%20-%20Light/6-01%20-%20The%20Electromagnetic%20Spectrum/image_12.png)

![image_13](6%20-%20Light/6-01%20-%20The%20Electromagnetic%20Spectrum/image_13.png)

![image_14](6%20-%20Light/6-01%20-%20The%20Electromagnetic%20Spectrum/image_14.png)

![image_15](6%20-%20Light/6-01%20-%20The%20Electromagnetic%20Spectrum/image_15.png)

![image_16](6%20-%20Light/6-01%20-%20The%20Electromagnetic%20Spectrum/image_16.png)

![image_17](6%20-%20Light/6-01%20-%20The%20Electromagnetic%20Spectrum/image_17.png)

![image_18](6%20-%20Light/6-01%20-%20The%20Electromagnetic%20Spectrum/image_18.png)

![image_19](6%20-%20Light/6-01%20-%20The%20Electromagnetic%20Spectrum/image_19.png)

![image_20](6%20-%20Light/6-01%20-%20The%20Electromagnetic%20Spectrum/image_20.png)

![image_21](6%20-%20Light/6-01%20-%20The%20Electromagnetic%20Spectrum/image_21.png)

---

1. Light from a particular source has a wavelength of 480 nm.
Find the frequency f of the light.

```js
const c = 3.0 * Math.pow(10, 8); // m/s
let wavelength = 480 * Math.pow(10, -9); // m
let f = c / wavelength; // Hz
console.log('f =', f.toExponential(), 'Hz');
// f = 6.249999999999999e+14 Hz
console.log('f =', Number(f.toPrecision(2)).toExponential(), 'Hz');
// f = 6.2e+14 Hz
```

---

2. Light from a particular source has a wavelength of 500 nm.
Find the frequency f of the light.

```js
const c = 3.0 * Math.pow(10, 8); // m/s
let wavelength = 500 * Math.pow(10, -9); // m
let f = c / wavelength; // Hz
console.log('f =', f.toExponential(), 'Hz');
// f = 5.999999999999999e+14 Hz
console.log('f =', Number(f.toPrecision(2)).toExponential(), 'Hz');
// f = 6e+14 Hz
```

---

3. Light from a particular source has a frequency of 6.0 x 10^14 Hz. Find the wavelength of the light.

```js
const c = 3.0 * Math.pow(10, 8); // m/s
let f = 6.0 * Math.pow(10, 14); // Hz
let wavelength = c / f; // m
console.log('wavelength =', wavelength.toExponential(), 'm');
// wavelength = 5e-7 m
```

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 61

---

### 6.02: Diffraction and Interference

---

![image_1](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_1.png)

![image_2](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_2.png)

![image_3](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_3.png)

![image_4](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_4.png)

![image_5](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_5.png)

![image_6](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_6.png)

![image_7](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_7.png)

![image_8](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_8.png)

![image_9](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_9.png)

![image_10](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_10.png)

![image_11](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_11.png)

![image_12](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_12.png)

![image_13](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_13.png)

![image_14](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_14.png)

![image_15](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_15.png)

![image_16](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_16.png)

![image_17](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_17.png)

![image_18](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_18.png)

![image_19](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_19.png)

![image_20](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_20.png)

![image_21](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_21.png)

![image_22](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_22.png)

![image_23](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_23.png)

![image_24](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_24.png)

![image_25](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_25.png)

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 62

---

### 6.03: Reflection

---

![image_1](6%20-%20Light/6-03%20-%20Reflection/image_1.png)

![image_2](6%20-%20Light/6-03%20-%20Reflection/image_2.png)

![image_3](6%20-%20Light/6-03%20-%20Reflection/image_3.png)

![image_4](6%20-%20Light/6-03%20-%20Reflection/image_4.png)

![image_5](6%20-%20Light/6-03%20-%20Reflection/image_5.png)

![image_6](6%20-%20Light/6-03%20-%20Reflection/image_6.png)

![image_7](6%20-%20Light/6-03%20-%20Reflection/image_7.png)

![image_8](6%20-%20Light/6-03%20-%20Reflection/image_8.png)

![image_9](6%20-%20Light/6-03%20-%20Reflection/image_9.png)

![image_10](6%20-%20Light/6-03%20-%20Reflection/image_10.png)

![image_11](6%20-%20Light/6-03%20-%20Reflection/image_11.png)

![image_12](6%20-%20Light/6-03%20-%20Reflection/image_12.png)

![image_13](6%20-%20Light/6-03%20-%20Reflection/image_13.png)

![image_14](6%20-%20Light/6-03%20-%20Reflection/image_14.png)

![image_15](6%20-%20Light/6-03%20-%20Reflection/image_15.png)

![image_16](6%20-%20Light/6-03%20-%20Reflection/image_16.png)

![image_17](6%20-%20Light/6-03%20-%20Reflection/image_17.png)

![image_18](6%20-%20Light/6-03%20-%20Reflection/image_18.png)

![image_19](6%20-%20Light/6-03%20-%20Reflection/image_19.png)

![image_20](6%20-%20Light/6-03%20-%20Reflection/image_20.png)

---

1. Flint glass has an index of refraction n = 1.66. What is the critical angle for light in the glass?

```js
const refraction_air = 1;
const refraction_glass = 1.66;
// sin(theta) = 1/1.66
let ratio = refraction_air / refraction_glass;
console.log('ratio =', ratio);
// ratio = 0.6024096385542169
console.log('ratio =', ratio.toPrecision(3));
// ratio = 0.602
let angle = Math.asin(ratio) * 180 / Math.PI; // degrees
console.log('angle =', angle, 'degrees');
// angle = 37.08506032429864 degrees
console.log('angle =', Math.round(angle), 'degrees');
// angle = 37 degrees
```

---

2. What is the index of refraction when the critical angle for light is 37 degrees?

```js
const refraction_air = 1;
const angle = 37; // degrees
let ratio = Math.sin(angle / 180 * Math.PI); // refraction index
console.log('ratio =', ratio);
let index = refraction_air / ratio;
console.log('index =', index, 'refraction index');
// index = 1.6616401411224833 refraction index
console.log('index =', index.toPrecision(3), 'refraction index');
// index = 1.66 refraction index
```

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 63

---

### 6.04: Refraction

---

![image_1](6%20-%20Light/6-04%20-%20Refraction/image_1.png)

![image_2](6%20-%20Light/6-04%20-%20Refraction/image_2.png)

![image_3](6%20-%20Light/6-04%20-%20Refraction/image_3.png)

![image_4](6%20-%20Light/6-04%20-%20Refraction/image_4.png)

![image_5](6%20-%20Light/6-04%20-%20Refraction/image_5.png)

![image_6](6%20-%20Light/6-04%20-%20Refraction/image_6.png)

![image_7](6%20-%20Light/6-04%20-%20Refraction/image_7.png)

![image_8](6%20-%20Light/6-04%20-%20Refraction/image_8.png)

![image_9](6%20-%20Light/6-04%20-%20Refraction/image_9.png)

![image_10](6%20-%20Light/6-04%20-%20Refraction/image_10.png)

![image_11](6%20-%20Light/6-04%20-%20Refraction/image_11.jpg)

![image_12](6%20-%20Light/6-04%20-%20Refraction/image_12.png)

![image_13](6%20-%20Light/6-04%20-%20Refraction/image_13.png)

![image_14](6%20-%20Light/6-04%20-%20Refraction/image_14.png)

![image_15](6%20-%20Light/6-04%20-%20Refraction/image_15.png)

![image_16](6%20-%20Light/6-04%20-%20Refraction/image_16.png)

![image_17](6%20-%20Light/6-04%20-%20Refraction/image_17.png)

![image_18](6%20-%20Light/6-04%20-%20Refraction/image_18.png)

---

1. Light with a wavelength of 580 nm enters water, which has an index of refraction of 1.33. Find the wavelength of the light in water.

```js
const wavelengthAir = 580 * Math.pow(10, -9); // m
const indexWater = 1.33;
let wavelengthWater = wavelengthAir / indexWater; // m
console.log('wavelengthWater =', wavelengthWater.toExponential(), 'm');
// wavelengthWater = 4.360902255639098e-7 m
console.log('wavelengthWater =', Number(wavelengthWater.toPrecision(3)).toExponential(), 'm');
// wavelengthWater = 4.36e-7 m
```

---

2. Show that it follows from Snell’s law that light bends toward the normal when it enters a medium with a higher refractive index and away from the normal when it enters a medium with a lower refractive index.

```js
// Light bends toward the normal surface when it enters a medium with a higher refractive index.
// Light bends away from the normal when it enters a medium with a lower refractive index.
//
// n1 * sin(A) = n2 * sin(B)
//
function calculateCriticalAngle(n1, n2) {
  const min = Math.min(n1, n2);
  const max = Math.max(n1, n2);
  let ratio = n1 / n2;
  let angle = Math.asin(min/max) * 180 / Math.PI; // degrees
  if (n1 > n2) {
    angle = -angle;
  }
  console.log('n1=', n1, 'n2=', n2, 'ratio =', ratio.toPrecision(3), 'angle=', Math.round(angle));
}

const index_air = 1.003;
const index_acrylic_glass = 1.5;
const index_flint_glass = 1.62;

console.log('n1 == n2:');
calculateCriticalAngle(index_air, index_air);
// n1= 1.003 n2= 1.003 ratio = 1.00 angle= 90
calculateCriticalAngle(index_acrylic_glass, index_acrylic_glass);
// n1= 1.5 n2= 1.5 ratio = 1.00 angle= 90
calculateCriticalAngle(index_flint_glass, index_flint_glass);
// n1= 1.62 n2= 1.62 ratio = 1.00 angle= 90

console.log('n1 < n2:');
calculateCriticalAngle(index_air, index_acrylic_glass);
// n1= 1.003 n2= 1.5 ratio = 0.669 angle= 42
calculateCriticalAngle(index_air, index_flint_glass);
// n1= 1.003 n2= 1.62 ratio = 0.619 angle= 38
calculateCriticalAngle(index_acrylic_glass, index_flint_glass);
// n1= 1.5 n2= 1.62 ratio = 0.926 angle= 68

console.log('n1 > n2:');
calculateCriticalAngle(index_acrylic_glass, index_air);
// n1= 1.5 n2= 1.003 ratio = 1.50 angle= -42
calculateCriticalAngle(index_flint_glass, index_air);
// n1= 1.62 n2= 1.003 ratio = 1.62 angle= -38
calculateCriticalAngle(index_flint_glass, index_acrylic_glass);
// n1= 1.62 n2= 1.5 ratio = 1.08 angle= -68
```

---

3. Suppose a beam of light enters a plate of crown glass at an angle of incidence of 30°. Find its angle of refraction.

```js
// n1 * sin(A) = n2 * sin(B)
function calculateRefractionAngle(n1, n2, deg1) {
  const min = Math.min(n1, n2);
  const max = Math.max(n1, n2);
  const rad1 = deg1 / 180 * Math.PI; // radians
  let ratio = min / max * Math.sin(rad1);
  let rad2 = Math.asin(ratio); // radians
  if (n1 > n2) {
    rad2 = -rad2;
  }
  let deg2 = rad2 * 180 / Math.PI; // degrees
  console.log('n1=', n1, 'n2=', n2, 'ratio =', ratio.toPrecision(3), 'deg1=', Math.round(deg1), 'deg2=', deg2.toPrecision(3));
}

const index_air = 1.003;
const index_crown_glass = 1.52;
const angle = 30; // degrees

calculateRefractionAngle(index_air, index_crown_glass, angle);
// n1= 1.003 n2= 1.52 ratio = 0.330 deg1= 30 deg2= 19.3

// The angle of refraction, as expected, is smaller than the incident angle of 30°, and the light bends toward the normal in entering the denser (higher n) medium.
```

---

4. A flat transparent piece of acrylic is at the bottom of a beaker of water, A beam of light passes through the water to strike the acrylic at an angle of incidence of 35°. What angle does the beam make with the normal to the acrylic surface as it travels inside the acrylic?

```js
// n1 * sin(A) = n2 * sin(B)
function calculateRefractionAngle(n1, n2, deg1) {
  const min = Math.min(n1, n2);
  const max = Math.max(n1, n2);
  const rad1 = deg1 / 180 * Math.PI; // radians
  let ratio = min / max * Math.sin(rad1);
  let rad2 = Math.asin(ratio); // radians
  if (n1 > n2) {
    rad2 = -rad2;
  }
  let deg2 = rad2 * 180 / Math.PI; // degrees
  console.log('n1=', n1, 'n2=', n2, 'ratio =', ratio.toPrecision(3), 'deg1=', Math.round(deg1), 'deg2=', deg2.toPrecision(3));
}

const index_water = 1.33;
const index_acrylic_glass = 1.5;
const angle = 35; // degrees

calculateRefractionAngle(index_water, index_acrylic_glass, angle);
// n1= 1.33 n2= 1.5 ratio = 0.509 deg1= 35 deg2= 30.6

// The beam of light is bent closer to the normal because it goes from a region of lower index of refraction to a region with a higher index of refraction.
```

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 64

---

### 6.05 Mirrors

---

![image_1](6%20-%20Light/6-05%20-%20Mirrors/image_1.png)

![image_2](6%20-%20Light/6-05%20-%20Mirrors/image_2.png)

![image_3](6%20-%20Light/6-05%20-%20Mirrors/image_3.png)

![image_4](6%20-%20Light/6-05%20-%20Mirrors/image_4.png)

![image_5](6%20-%20Light/6-05%20-%20Mirrors/image_5.png)

![image_6](6%20-%20Light/6-05%20-%20Mirrors/image_6.png)

![image_7](6%20-%20Light/6-05%20-%20Mirrors/image_7.png)

![image_8](6%20-%20Light/6-05%20-%20Mirrors/image_8.png)

![image_9](6%20-%20Light/6-05%20-%20Mirrors/image_9.png)

![image_10](6%20-%20Light/6-05%20-%20Mirrors/image_10.png)

![image_11](6%20-%20Light/6-05%20-%20Mirrors/image_11.png)

![image_12](6%20-%20Light/6-05%20-%20Mirrors/image_12.png)

![image_13](6%20-%20Light/6-05%20-%20Mirrors/image_13.png)

![image_14](6%20-%20Light/6-05%20-%20Mirrors/image_14.png)

![image_15](6%20-%20Light/6-05%20-%20Mirrors/image_15.png)

![image_16](6%20-%20Light/6-05%20-%20Mirrors/image_16.png)

![image_17](6%20-%20Light/6-05%20-%20Mirrors/image_17.png)

![image_18](6%20-%20Light/6-05%20-%20Mirrors/image_18.png)

![image_19](6%20-%20Light/6-05%20-%20Mirrors/image_19.png)

![image_20](6%20-%20Light/6-05%20-%20Mirrors/image_20.png)

![image_21](6%20-%20Light/6-05%20-%20Mirrors/image_21.png)

![image_22](6%20-%20Light/6-05%20-%20Mirrors/image_22.png)

![image_23](6%20-%20Light/6-05%20-%20Mirrors/image_23.png)

![image_24](6%20-%20Light/6-05%20-%20Mirrors/image_24.png)

![image_25](6%20-%20Light/6-05%20-%20Mirrors/image_25.png)

![image_26](6%20-%20Light/6-05%20-%20Mirrors/image_26.png)

![image_27](6%20-%20Light/6-05%20-%20Mirrors/image_27.png)

![image_28](6%20-%20Light/6-05%20-%20Mirrors/image_28.png)

![image_29](6%20-%20Light/6-05%20-%20Mirrors/image_29.png)

![image_30](6%20-%20Light/6-05%20-%20Mirrors/image_30.png)

![image_31](6%20-%20Light/6-05%20-%20Mirrors/image_31.png)

![image_32](6%20-%20Light/6-05%20-%20Mirrors/image_32.png)

![image_33](6%20-%20Light/6-05%20-%20Mirrors/image_33.png)

![image_34](6%20-%20Light/6-05%20-%20Mirrors/image_34.png)

---

1. What is the radius given the focal length of 25 mm?

```js
let focalLength = 0.025; // m
let radius = 2 * focalLength; // m
console.log('radius', radius, 'm');
// radius 0.05 m
```

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 65

---

## 6.06: Lenses

---

![image_1](6%20-%20Light/6-06%20-%20Lenses/image_1.png)

![image_2](6%20-%20Light/6-06%20-%20Lenses/image_2.png)

![image_3](6%20-%20Light/6-06%20-%20Lenses/image_3.png)

![image_4](6%20-%20Light/6-06%20-%20Lenses/image_4.png)

![image_5](6%20-%20Light/6-06%20-%20Lenses/image_5.png)

![image_6](6%20-%20Light/6-06%20-%20Lenses/image_6.png)

![image_7](6%20-%20Light/6-06%20-%20Lenses/image_7.png)

![image_8](6%20-%20Light/6-06%20-%20Lenses/image_8.png)

![image_9](6%20-%20Light/6-06%20-%20Lenses/image_9.png)

![image_10](6%20-%20Light/6-06%20-%20Lenses/image_10.png)

![image_11](6%20-%20Light/6-06%20-%20Lenses/image_11.png)

![image_12](6%20-%20Light/6-06%20-%20Lenses/image_12.png)

![image_13](6%20-%20Light/6-06%20-%20Lenses/image_13.png)

![image_14](6%20-%20Light/6-06%20-%20Lenses/image_14.png)

![image_15](6%20-%20Light/6-06%20-%20Lenses/image_15.png)

![image_16](6%20-%20Light/6-06%20-%20Lenses/image_16.png)

![image_17](6%20-%20Light/6-06%20-%20Lenses/image_17.png)

![image_18](6%20-%20Light/6-06%20-%20Lenses/image_18.png)

![image_19](6%20-%20Light/6-06%20-%20Lenses/image_19.png)

![image_20](6%20-%20Light/6-06%20-%20Lenses/image_20.png)

![image_21](6%20-%20Light/6-06%20-%20Lenses/image_21.png)

![image_22](6%20-%20Light/6-06%20-%20Lenses/image_22.png)

![image_23](6%20-%20Light/6-06%20-%20Lenses/image_23.png)

![image_24](6%20-%20Light/6-06%20-%20Lenses/image_24.png)

![image_25](6%20-%20Light/6-06%20-%20Lenses/image_25.png)

![image_26](6%20-%20Light/6-06%20-%20Lenses/image_26.png)

![image_27](6%20-%20Light/6-06%20-%20Lenses/image_27.png)

![image_28](6%20-%20Light/6-06%20-%20Lenses/image_28.png)

![image_29](6%20-%20Light/6-06%20-%20Lenses/image_29.png)

![image_30](6%20-%20Light/6-06%20-%20Lenses/image_30.png)

![image_31](6%20-%20Light/6-06%20-%20Lenses/image_31.png)

![image_32](6%20-%20Light/6-06%20-%20Lenses/image_32.png)

![image_33](6%20-%20Light/6-06%20-%20Lenses/image_33.png)

![image_34](6%20-%20Light/6-06%20-%20Lenses/image_34.png)

![image_35](6%20-%20Light/6-06%20-%20Lenses/image_35.png)

![image_36](6%20-%20Light/6-06%20-%20Lenses/image_36.png)

![image_37](6%20-%20Light/6-06%20-%20Lenses/image_37.png)

![image_38](6%20-%20Light/6-06%20-%20Lenses/image_38.png)

![image_39](6%20-%20Light/6-06%20-%20Lenses/image_39.png)

![image_40](6%20-%20Light/6-06%20-%20Lenses/image_40.png)

![image_41](6%20-%20Light/6-06%20-%20Lenses/image_41.png)

![image_42](6%20-%20Light/6-06%20-%20Lenses/image_42.png)

![image_43](6%20-%20Light/6-06%20-%20Lenses/image_43.png)

![image_44](6%20-%20Light/6-06%20-%20Lenses/image_44.png)

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 66

---

## 7: Electric Forces

---

### 7.01: Static Electricity

---

![image_1](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_1.png)

![image_2](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_2.png)

![image_3](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_3.png)

![image_4](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_4.jpg)

![image_5](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_5.jpg)

![image_6](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_6.jpg)

![image_7](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_7.jpg)

![image_8](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_8.jpg)

![image_9](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_9.png)

![image_10](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_10.png)

![image_11](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_11.png)

![image_12](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_12.png)

![image_13](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_13.png)

![image_14](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_14.png)

![image_15](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_15.png)

![image_16](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_16.png)

![image_17](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_17.png)

![image_18](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_18.png)

![image_19](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_19.png)

![image_20](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_20.png)

![image_21](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_21.png)

![image_22](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_22.png)

![image_23](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_23.png)

![image_24](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_24.png)

![image_25](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_25.png)

![image_26](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_26.png)

![image_27](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_27.png)

![image_28](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_28.png)

![image_29](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_29.png)

![image_30](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_30.png)

![image_31](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_31.png)

![image_32](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_32.png)

![image_33](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_33.png)

![image_34](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_34.png)

![image_35](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_35.png)

![image_36](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_36.png)

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 67

---

### 7.02: Electric Force

---

![image_1](7%20-%20Electric%20Forces/7-02%20-%20Electric%20Force/image_1.png)

![image_2](7%20-%20Electric%20Forces/7-02%20-%20Electric%20Force/image_2.png)

![image_3](7%20-%20Electric%20Forces/7-02%20-%20Electric%20Force/image_3.png)

![image_4](7%20-%20Electric%20Forces/7-02%20-%20Electric%20Force/image_4.png)

![image_5](7%20-%20Electric%20Forces/7-02%20-%20Electric%20Force/image_5.png)

![image_6](7%20-%20Electric%20Forces/7-02%20-%20Electric%20Force/image_6.png)

![image_7](7%20-%20Electric%20Forces/7-02%20-%20Electric%20Force/image_7.png)

![image_8](7%20-%20Electric%20Forces/7-02%20-%20Electric%20Force/image_8.png)

![image_9](7%20-%20Electric%20Forces/7-02%20-%20Electric%20Force/image_9.png)

![image_10](7%20-%20Electric%20Forces/7-02%20-%20Electric%20Force/image_10.png)

![image_11](7%20-%20Electric%20Forces/7-02%20-%20Electric%20Force/image_11.png)

![image_12](7%20-%20Electric%20Forces/7-02%20-%20Electric%20Force/image_12.png)

![image_13](7%20-%20Electric%20Forces/7-02%20-%20Electric%20Force/image_13.png)

![image_14](7%20-%20Electric%20Forces/7-02%20-%20Electric%20Force/image_14.png)

![image_15](7%20-%20Electric%20Forces/7-02%20-%20Electric%20Force/image_15.png)

![image_16](7%20-%20Electric%20Forces/7-02%20-%20Electric%20Force/image_16.png)

![image_17](7%20-%20Electric%20Forces/7-02%20-%20Electric%20Force/image_17.png)

![image_18](7%20-%20Electric%20Forces/7-02%20-%20Electric%20Force/image_18.png)

---

```js
// Coulomb's constant
const k = 9.0 * Math.pow(10, 9); // N * m^2 / C^2

//  Coulomb's law
F = k * q1 * q2 / Math.pow(r, 2);

// Newton’s Law of Universal Gravitation
F = G * m1 * m2 / Math.pow(r, 2);
```

* A charge of −1C negative 1 C is the equivalent of the electric force exerted by 6.24 x 10^18 electrons.

* A charge of +1C is the equivalent of 6.24 x 10^18 protons.

* One electron has a force of −1.6 × 10^-19 C

* One proton has a force of 1.6 × 10^-19 C

*  If two objects are 1 meter apart and each has a charge of +1 coulomb, the repelling force between them is an astounding 9 × 10^9 N, which is about 900,000 tons of force.

* A single lightning bolt has an electric charge ranging from 5 C to 10 C.

---

1. A negative charge of −2.0 x 10^−4 C
and a positive charge of +4.0 × 10^−4 C are separated by 0.20 m. What is the magnitude and direction of the force between them?

```js

let q1 = -2.0 * Math.pow(10, -4); // C
let q2 = 4.0 * Math.pow(10, -4); // C
let r = 0.2; // m

// Coulomb's constant
const k = 9.0 * Math.pow(10, 9); // N * m^2 / C^2

//  Coulomb's law
let F = k * q1 * q2 / Math.pow(r, 2);
console.log('F =', F, 'N');
// F = -17999.999999999993 N
console.log('F =', F.toPrecision(2), 'N');
// F = -1.8e+4 N
```

* This is an attractive force as indicated by the fact that the value is negative.

---

2. What would happen if the distance was doubled?

```js
let q1 = -2.0 * Math.pow(10, -4); // C
let q2 = 4.0 * Math.pow(10, -4); // C
let r = 0.4; // m

// Coulomb's constant
const k = 9.0 * Math.pow(10, 9); // N * m^2 / C^2

//  Coulomb's law
let F = k * q1 * q2 / Math.pow(r, 2);
console.log('F =', F, 'N');
// F = -4499.999999999998 N
console.log('F =', F.toPrecision(2), 'N');
// F = -4.5e+3 N
```

* This is an attractive force as indicated by the fact that the value is negative.

---

3. A charge of –2.0 × 10^–4 C and a charge of +4.0 × 10^–4 C are separated by 0.40 m. What is the magnitude and direction of the force between them?

```js
let q1 = -2.0 * Math.pow(10, -4); // C
let q2 = 4.0 * Math.pow(10, -4); // C
let r = 0.4; // m

// Coulomb's constant
const k = 9.0 * Math.pow(10, 9); // N * m^2 / C^2

//  Coulomb's law
let F = k * q1 * q2 / Math.pow(r, 2);
console.log('F =', F, 'N');
// F = -4499.999999999998 N
console.log('F =', F.toPrecision(2), 'N');
// F = -4.5e+3 N
```

* Because the force is negative, the direction of the force is toward the other charge. You can confirm this by looking at the signs of the original charges. Because the two charges have opposite signs, they will attract each other.

---

4. Object A has a charge of +6.0 x 10^-6 C, while Object B has a charge of +3.0 x 10^-6 C. If the force between them is 1.8 x 10^2 N, then how far apart are they?

```js
let q1 = 6.0 * Math.pow(10, -6); // C
let q2 = 3.0 * Math.pow(10, -6); // C
let F = 1.8 * Math.pow(10, 2); // N

// Coulomb's constant
const k = 9.0 * Math.pow(10, 9); // N * m^2 / C^2

let r = Math.sqrt(k * q1 * q2 / F); // m
console.log('r =', r, 'm');
// r = 0.03 m
console.log('r =', r.toPrecision(2), 'm');
// r = 0.03 m
console.log('r =', r.toExponential(), 'm');
// r = 3e-2 m
```

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 68

---

### 7.03: Electric Fields

---

![image_1](7%20-%20Electric%20Forces/7-03%20-%20Electric%20Fields/image_1.png)

![image_2](7%20-%20Electric%20Forces/7-03%20-%20Electric%20Fields/image_2.png)

![image_3](7%20-%20Electric%20Forces/7-03%20-%20Electric%20Fields/image_3.png)

![image_4](7%20-%20Electric%20Forces/7-03%20-%20Electric%20Fields/image_4.png)

![image_5](7%20-%20Electric%20Forces/7-03%20-%20Electric%20Fields/image_5.png)

![image_6](7%20-%20Electric%20Forces/7-03%20-%20Electric%20Fields/image_6.png)

![image_7](7%20-%20Electric%20Forces/7-03%20-%20Electric%20Fields/image_7.png)

![image_8](7%20-%20Electric%20Forces/7-03%20-%20Electric%20Fields/image_8.png)

![image_9](7%20-%20Electric%20Forces/7-03%20-%20Electric%20Fields/image_9.png)

![image_10](7%20-%20Electric%20Forces/7-03%20-%20Electric%20Fields/image_10.png)

![image_11](7%20-%20Electric%20Forces/7-03%20-%20Electric%20Fields/image_11.png)

![image_12](7%20-%20Electric%20Forces/7-03%20-%20Electric%20Fields/image_12.png)

![image_13](7%20-%20Electric%20Forces/7-03%20-%20Electric%20Fields/image_13.png)

![image_14](7%20-%20Electric%20Forces/7-03%20-%20Electric%20Fields/image_14.png)

![image_15](7%20-%20Electric%20Forces/7-03%20-%20Electric%20Fields/image_15.png)

---

```js
// For a test charge q_prime
F = K * q_prime * Q / Math.pow(r, 2); // N

// strength of the field
E = F / q_prime; // N/C

// substition
E = K * Q / Math.pow(r, 2);
```

---

1. A positive test charge of 4.0 x 10^–6 C experiences a force of –0.060 N at an angle of 20° from a source charge. What is the strength and direction of the electric field?

```js
let q_prime = 4.0 * Math.pow(10, -6); // C
let F = -0.060; // N
let E = F / q_prime; // N/C
console.log('E =', E, 'N/C');
// E = -15000 N/C
console.log('E =', E.toPrecision(2), 'N/C');
// E = -1.5e+4 N/C
let originalAngle = 20; // degrees
let minAngle = 180; // degrees
let maxAngle = (180 + originalAngle) % 360; // degrees
console.log('minAngle =', minAngle, 'degrees');
// minAngle = 180 degrees
console.log('maxAngle =', maxAngle, 'degrees');
// maxAngle = 200 degrees
```

* When the force is negative, E is negative, which indicates that the direction of the field is inward and that the source charge is negative. The angle of the force would be 180° from the original angle, or 200°.

---

2. The strength of an electric field at 1.00 m from a source charge is –1.00 × 10^4 N/C. What is the magnitude of the source charge?

```js
let E = -1.00 * Math.pow(10, 4); // N/C
let r = 1.00; // m
let k = 9.00 * Math.pow(10, 9); // N*m^2/C^2
let Q = E * Math.pow(r, 2) / k; // C
console.log('Q =', Q.toExponential(), 'C');
// Q = -1.111111111111111e-6
console.log('Q =', Number(Q.toPrecision(3)).toExponential(), 'C');
// Q = -1.11e-6 C
```

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 69

---

### 7.07: Electric Potential Difference

---

![image_1](7%20-%20Electric%20Forces/7-07%20-%20Electric%20Potential%20Difference/image_1.png)

![image_2](7%20-%20Electric%20Forces/7-07%20-%20Electric%20Potential%20Difference/image_2.png)

![image_3](7%20-%20Electric%20Forces/7-07%20-%20Electric%20Potential%20Difference/image_3.png)

![image_4](7%20-%20Electric%20Forces/7-07%20-%20Electric%20Potential%20Difference/image_4.png)

![image_5](7%20-%20Electric%20Forces/7-07%20-%20Electric%20Potential%20Difference/image_5.png)

![image_6](7%20-%20Electric%20Forces/7-07%20-%20Electric%20Potential%20Difference/image_6.png)

![image_7](7%20-%20Electric%20Forces/7-07%20-%20Electric%20Potential%20Difference/image_7.png)

![image_8](7%20-%20Electric%20Forces/7-07%20-%20Electric%20Potential%20Difference/image_8.png)

![image_9](7%20-%20Electric%20Forces/7-07%20-%20Electric%20Potential%20Difference/image_9.png)

![image_10](7%20-%20Electric%20Forces/7-07%20-%20Electric%20Potential%20Difference/image_10.png)

![image_11](7%20-%20Electric%20Forces/7-07%20-%20Electric%20Potential%20Difference/image_11.png)

![image_12](7%20-%20Electric%20Forces/7-07%20-%20Electric%20Potential%20Difference/image_12.png)

![image_13](7%20-%20Electric%20Forces/7-07%20-%20Electric%20Potential%20Difference/image_13.png)

![image_14](7%20-%20Electric%20Forces/7-07%20-%20Electric%20Potential%20Difference/image_14.png)

![image_15](7%20-%20Electric%20Forces/7-07%20-%20Electric%20Potential%20Difference/image_15.png)

![image_16](7%20-%20Electric%20Forces/7-07%20-%20Electric%20Potential%20Difference/image_16.png)

---

1. If an electric potential difference of 200.0 V occurs when a point charge of 1.0 μC is moved within an electric field, then what is the change in potential energy?

```js
let DV = 200.0; // V
let q = 1.0 * Math.pow(10, -6); // C
let DUe = q * DV; // J
console.log('DUe =', DUe.toExponential(), 'J');
// DUe = 1.9999999999999998e-4 J
console.log('DUe =', Number(DUe.toPrecision(2)).toExponential(), 'J');
// DUe = 2e-4 J
```

---

2. If 200.0 J of work is done to a point charge of 1.0 μC that is moved within an electric field, then what is the change in electric potential difference?

```js
let W = 200.0; // J
let q = 1.0 * Math.pow(10, -6); // C
let DV = W / q; // V
console.log('DV =', DV.toPrecision(2), 'V');
// DV = 2.0e+8 V
```

---

3. Two large parallel plates are 10.0 cm apart. The strength of the electric field between them is 500.0 N/C. What is the electric potential difference (ΔV) between them? How does this compare with the electric potential difference when the plates were 5.0 cm apart?

```js
let d = 0.10; // m
let E = 500.0; // N/C
let DV = E * d; // V
console.log('DV =', DV.toPrecision(2), 'V');
// DV = 50 V
```

```js
let d = 0.05; // m
let E = 500.0; // N/C
let DV = E * d; // V
console.log('DV =', DV.toPrecision(2), 'V');
// DV = 25 V
```

* ΔV doubled compared to when the plates were 5.0 cm apart.

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 70

---

## 8: Currents and Circuits

---

### 8.01: Currents and Circuits

---

![image_1](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_1.png)

![image_2](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_2.png)

![image_3](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_3.png)

![image_4](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_4.png)

![image_5](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_5.png)

![image_6](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_6.png)

![image_7](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_7.png)

![image_8](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_8.png)

![image_9](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_9.png)

![image_10](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_10.png)

![image_11](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_11.png)

![image_12](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_12.png)

![image_13](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_13.png)

![image_14](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_14.png)

![image_15](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_15.png)

![image_16](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_16.png)

![image_17](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_17.png)

![image_18](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_18.png)

![image_19](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_19.png)

![image_20](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_20.png)

![image_21](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_21.png)

![image_22](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_22.png)

![image_23](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_23.png)

![image_24](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_24.png)

![image_25](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_25.png)

![image_26](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_26.png)

![image_27](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_27.png)

![image_28](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_28.png)

![image_29](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_29.png)

---

1. If 20 C of charge passes a point in 5 s, what is the magnitude of the electric current?

```js
let q = 20; // C
let t = 5; // s
let I = q / t; // A
console.log('I =', I, 'A');
// I = 4 A
```

---

2. A light bulb in a lamp uses 0.55 A of current when a voltage of 110 V is applied to it. How much power does the electric light bulb use?

```js
let I = 0.55; // A
let DV = 110; // V
let P = I * DV; // W
console.log('P =', P, 'W');
// P = 60.50000000000001 W
console.log('P =', Number(P.toPrecision(1)), 'W');
// P = 60 W
```

---

3. An electric oven has a power supply of 220 V and a power rating of 7.3 kW. How much electric current does it draw?

```js
let DV = 220; // V
let P = 7300; // W
let I = P / DV; // A
console.log('I =', I, 'A');
// I = 33.18181818181818 A
console.log('I =', I.toPrecision(2), 'A');
// I = 33 A
```

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 71

---

### 8.02: Current Electric Forces

---

![image_1](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_1.png)

![image_2](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_2.png)

![image_3](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_3.png)

![image_4](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_4.png)

![image_5](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_5.png)

![image_6](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_6.png)

![image_7](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_7.png)

![image_8](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_8.png)

![image_9](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_9.png)

![image_10](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_10.png)

![image_11](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_11.png)

![image_12](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_12.png)

![image_13](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_13.png)

![image_14](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_14.png)

![image_15](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_15.png)

![image_16](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_16.png)

![image_17](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_17.png)

![image_18](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_18.png)

![image_19](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_19.png)

![image_20](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_20.png)

![image_21](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_21.png)

![image_22](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_22.png)

![image_23](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_23.png)

![image_24](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_24.png)

![image_25](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_25.png)

![image_26](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_26.png)

![image_27](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_27.png)

![image_28](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_28.png)

![image_29](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_29.png)

---

1. A 30.0 V battery maintains a current of 3.0 A through a resistor. What is value of the electric resistance?

```js
let DV = 30.0; // V
let I = 3.0; // A
let R = DV / I; // ohmms
console.log('R =', R, 'ohm');
// R = 10 ohm
console.log('R =', R.toFixed(1), 'ohm');
// R = 10.0 ohm
```

---

2. If a heater has a resistance of 5.0 Ω and draws 12.0 A, then what power does it consume?

```js
let I = 12.0; // A
let R = 5.0; // ohm
let P = Math.pow(I, 2) * R; // W
console.log('P =', P, 'W');
// P = 720 W
```

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 72

---

### 8.03: Series Circuits

---

![image_1](8%20-%20Currents%20and%20Circuits/8-03%20-%20Series%20Circuits/image_1.png)

![image_2](8%20-%20Currents%20and%20Circuits/8-03%20-%20Series%20Circuits/image_2.png)

![image_3](8%20-%20Currents%20and%20Circuits/8-03%20-%20Series%20Circuits/image_3.png)

![image_4](8%20-%20Currents%20and%20Circuits/8-03%20-%20Series%20Circuits/image_4.png)

![image_5](8%20-%20Currents%20and%20Circuits/8-03%20-%20Series%20Circuits/image_5.png)

![image_6](8%20-%20Currents%20and%20Circuits/8-03%20-%20Series%20Circuits/image_6.png)

![image_7](8%20-%20Currents%20and%20Circuits/8-03%20-%20Series%20Circuits/image_7.png)

![image_8](8%20-%20Currents%20and%20Circuits/8-03%20-%20Series%20Circuits/image_8.png)

![image_9](8%20-%20Currents%20and%20Circuits/8-03%20-%20Series%20Circuits/image_9.png)

![image_10](8%20-%20Currents%20and%20Circuits/8-03%20-%20Series%20Circuits/image_10.png)

![image_11](8%20-%20Currents%20and%20Circuits/8-03%20-%20Series%20Circuits/image_11.png)

![image_12](8%20-%20Currents%20and%20Circuits/8-03%20-%20Series%20Circuits/image_12.png)

![image_13](8%20-%20Currents%20and%20Circuits/8-03%20-%20Series%20Circuits/image_13.png)

![image_14](8%20-%20Currents%20and%20Circuits/8-03%20-%20Series%20Circuits/image_14.png)

---

1. A 12.0 volt battery maintains a current through a light bulb that has a resistance of 2.0 Ω. What is the current and power in the circuit?

```js
let DV = 12.0; // V
let R = 2.0; // ohm
let I = DV / R; // A
console.log('I =', I, 'A');
// I = 6 A
console.log('I =', I.toFixed(1), 'A');
// I = 6.0 A
let P = I * DV; // W
console.log('P =', P, 'W');
// P = 72 W
```

---

2. A 12.0 volt battery maintains a current through two light bulbs, each of which has a resistance of 2.0 Ω. What is the current and power in the circuit?

```js
let DV = 12.0; // V
let R1 = 2.0; // ohm
let R2 = 2.0; // ohm
let Req = R1 + R2; // ohm
console.log('Req =', Req, 'ohm');
// Req = 4 ohm
let I = DV / Req; // A
console.log('I =', I, 'A');
// I = 3 A
console.log('I =', I.toFixed(1), 'A');
// I = 3.0 A
let P = I * DV; // W
console.log('P =', P, 'W');
// P = 36 W
```

---

3. A 12.0 volt battery maintains a current through three light bulbs, each of which has a resistance of 2.0 Ω. What is the current and power in the circuit?

```js
let DV = 12.0; // V
let R1 = 2.0; // ohm
let R2 = 2.0; // ohm
let R3 = 2.0; // ohm
let Req = R1 + R2 + R3; // ohm
console.log('Req =', Req, 'ohm');
// Req = 6 ohm
let I = DV / Req; // A
console.log('I =', I, 'A');
// I = 2 A
console.log('I =', I.toFixed(1), 'A');
// I = 2.0 A
let P = I * DV; // W
console.log('P =', P, 'W');
// P = 24 W
```

---

4. A 12.0 V battery is hooked up to three resistors in series. The first resistor is 2.0 Ω, the second is 3.0 Ω, and the third is 5.0 Ω. What is the current in the circuit? What is the total power? How much voltage drops across each resistor?

```js
let DVtotal = 12.0; // V
let R1 = 2.0; // ohm
let R2 = 3.0; // ohm
let R3 = 5.0; // ohm
let Req = R1 + R2 + R3; // ohm
console.log('Req =', Req, 'ohm');
// Req = 10 ohm
let Itotal = DVtotal / Req; // A
console.log('Itotal =', Itotal, 'A');
// Itotal = 1.2 A
console.log('Itotal =', Itotal.toFixed(2), 'A');
// Itotal = 1.20 A
let P = Itotal * DVtotal; // W
console.log('P =', P, 'W');
// P = 14.399999999999999 W
console.log('P =', P.toPrecision(3), 'W');
// P = 14.4 W
let DV1 = Itotal * R1; // V
console.log('DV1 =', DV1, 'V');
// DV1 = 2.4 V
let DV2 = Itotal * R2; // V
console.log('DV2 =', DV2, 'V');
// DV2 = 3.5999999999999996 V
console.log('DV2 =', DV2.toFixed(1), 'V');
// DV2 = 3.6 V
let DV3 = Itotal * R3; // V
console.log('DV3 =', DV3, 'V');
// DV3 = 6 V
console.log('DV3 =', DV3.toFixed(1), 'V');
// DV3 = 6.0 V
DVtotal123 = DV1 + DV2 + DV3;
console.log('DVtotal123 =', DVtotal123, 'V');
// DVtotal123 = 12 V
```

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 73

---

### 8.04: Parallel Circuits

---

![image_1](8%20-%20Currents%20and%20Circuits/8-04%20-%20Parallel%20Circuits/image_1.png)

![image_2](8%20-%20Currents%20and%20Circuits/8-04%20-%20Parallel%20Circuits/image_2.png)

![image_3](8%20-%20Currents%20and%20Circuits/8-04%20-%20Parallel%20Circuits/image_3.png)

![image_4](8%20-%20Currents%20and%20Circuits/8-04%20-%20Parallel%20Circuits/image_4.png)

![image_5](8%20-%20Currents%20and%20Circuits/8-04%20-%20Parallel%20Circuits/image_5.png)

![image_6](8%20-%20Currents%20and%20Circuits/8-04%20-%20Parallel%20Circuits/image_6.png)

![image_7](8%20-%20Currents%20and%20Circuits/8-04%20-%20Parallel%20Circuits/image_7.png)

![image_8](8%20-%20Currents%20and%20Circuits/8-04%20-%20Parallel%20Circuits/image_8.png)

![image_9](8%20-%20Currents%20and%20Circuits/8-04%20-%20Parallel%20Circuits/image_9.png)

![image_10](8%20-%20Currents%20and%20Circuits/8-04%20-%20Parallel%20Circuits/image_10.png)

![image_11](8%20-%20Currents%20and%20Circuits/8-04%20-%20Parallel%20Circuits/image_11.png)

![image_12](8%20-%20Currents%20and%20Circuits/8-04%20-%20Parallel%20Circuits/image_12.png)

![image_13](8%20-%20Currents%20and%20Circuits/8-04%20-%20Parallel%20Circuits/image_13.png)

![image_14](8%20-%20Currents%20and%20Circuits/8-04%20-%20Parallel%20Circuits/image_14.png)

---

1. A 12.0 volt battery maintains a current through a light bulb that has a resistance of 2.0 Ω. What is the current and power in the circuit?

```js
let DV = 12.0; // V
let R = 2.0; // ohm
let I = DV / R; // A
console.log('I =', I, 'A');
// I = 6 A
console.log('I =', I.toFixed(1), 'A');
// I = 6.0 A
let P = I * DV; // W
console.log('P =', P, 'W');
// P = 72 W
```

---

2. A 12.0 volt battery maintains a current through two light bulbs arranged in parallel, each of which has a resistance of 2.0 Ω. What is the current and power in the circuit?

```js
let DV = 12.0; // V
let R = 2.0; // ohm
let Req = 1 / (1 / R + 1 / R); // ohm
console.log('Req =', Req, 'ohm');
let I = DV / Req; // A
console.log('I =', I, 'A');
// I = 12 A
console.log('I =', I.toFixed(1), 'A');
// I = 12.0 A
let P = I * DV; // W
console.log('P =', P, 'W');
// P = 144 W
```

---

3. A 12.0 volt battery maintains a current through three light bulbs arranged in parallel, each of which has a resistance of 2.0 Ω. What is the current and power in the circuit?

```js
let DV = 12.0; // V
let R = 2.0; // ohm
let Req = 1 / (1 / R + 1 / R + 1 / R); // ohm
console.log('Req =', Req, 'ohm');
// Req = 0.6666666666666666 ohm
console.log('Req =', Req.toFixed(2), 'ohm');
// Req = 0.67 ohm
let I = DV / Req; // A
console.log('I =', I, 'A');
// I = 18 A
console.log('I =', I.toFixed(1), 'A');
// I = 18.0 A
let P = I * DV; // W
console.log('P =', P, 'W');
// P = 216 W
```

---

4. A 12.0 V battery is hooked up to three resistors in parallel. The first resistor is 2.0 Ω, the second is 3.0 Ω, and the third is 5.0 Ω. What is the current in the circuit? What is the total power? How much current goes through each resistor?

```js
let DVtotal = 12.0; // V
let R1 = 2.0; // ohm
let R2 = 3.0; // ohm
let R3 = 5.0; // ohm
let Req = 1 / (1 / R1 + 1 / R2 + 1 / R3); // ohm
console.log('Req =', Req, 'ohm');
// Req = 10 ohm
console.log('Req =', Req.toFixed(2), 'ohm');
// Req = 0.97 ohm
let Itotal = DVtotal / Req; // A
console.log('Itotal =', Itotal, 'A');
// Itotal = 12.399999999999999 A
console.log('Itotal =', Itotal.toPrecision(2), 'A');
// Itotal = 12 A
Itotal = Number(Itotal.toPrecision(2));
let Ptotal = Itotal * DVtotal; // W
console.log('Ptotal =', Ptotal, 'W');
// Ptotal = 144 W
let l1 = DVtotal / R1; // A
console.log('l1 =', l1, 'A');
// l1 = 6 A
console.log('l1 =', l1.toFixed(1), 'A');
// l1 = 6.0 A
let l2 = DVtotal / R2; // A
console.log('l2 =', l2, 'A');
// l2 = 4 A
console.log('l2 =', l2.toFixed(1), 'A');
// l2 = 4.0 A
let l3 = DVtotal / R3; // A
console.log('l3 =', l3, 'A');
// l3 = 2.4 A
let ltotal = l1 + l2 + l3; // A
console.log('ltotal =', ltotal, 'A');
// ltotal = 12.4 A
console.log('ltotal =', Number(ltotal.toPrecision(2)), 'A');
// ltotal = 12 A
```

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 74

---

### 8.05: Combined Circuits

---

![image_1](8%20-%20Currents%20and%20Circuits/8-05%20-%20Combined%20Circuits/image_1.png)

![image_2](8%20-%20Currents%20and%20Circuits/8-05%20-%20Combined%20Circuits/image_2.png)

![image_3](8%20-%20Currents%20and%20Circuits/8-05%20-%20Combined%20Circuits/image_3.png)

![image_6](8%20-%20Currents%20and%20Circuits/8-05%20-%20Combined%20Circuits/image_6.png)

![image_7](8%20-%20Currents%20and%20Circuits/8-05%20-%20Combined%20Circuits/image_7.png)

![image_8](8%20-%20Currents%20and%20Circuits/8-05%20-%20Combined%20Circuits/image_8.png)

![image_9](8%20-%20Currents%20and%20Circuits/8-05%20-%20Combined%20Circuits/image_9.png)

![image_10](8%20-%20Currents%20and%20Circuits/8-05%20-%20Combined%20Circuits/image_10.png)

---

1. What is the equivalent resistance of a combined circuit with the arrangement of resistors shown? Calculate the total current moving through the circuit.

![image_4](8%20-%20Currents%20and%20Circuits/8-05%20-%20Combined%20Circuits/image_4.png)

```js
let R1 = 10.0; // ohm
let R2 = 13.0; // ohm
let R3 = 15.0; // ohm
let R4 = 35.0; // ohm
let DVtotal = 60.0; // V
let R_2_3 = 1 / (1 / R2 + 1 / R3); // ohm
console.log('R_2_3 =', R_2_3, 'ohm');
// R_2_3 = 6.964285714285714 ohm
console.log('R_2_3 =', R_2_3.toFixed(1), 'ohm');
// R_2_3 = 7.0 ohm
let Req = R1 + R_2_3 + R4; // ohm
console.log('Req =', Req, 'ohm');
// Req = 51.964285714285715 ohm
console.log('Req =', Req.toFixed(1), 'ohm');
// Req = 52.0 ohm
let ltotal = DVtotal / Req; // A
console.log('ltotal =', ltotal, 'A')
// ltotal = 1.1546391752577319 A
console.log('ltotal =', ltotal.toFixed(2), 'A');
// ltotal = 1.15 A
```

---

2. What is the equivalent resistance of a combined circuit with the arrangement of resistors shown? Calculate the total current moving through the circuit.

![image_5](8%20-%20Currents%20and%20Circuits/8-05%20-%20Combined%20Circuits/image_5.png)

```js
let R1 = 10.0; // ohm
let R_2_3 = 7.0; // ohm
let R4 = 35.0; // ohm
let ltotal = 1.15; // A
let DV1 = ltotal * R1; // V
console.log('DV1 =', DV1, 'V');
// DV1 = 11.5 V
console.log('DV1 =', DV1.toPrecision(3), 'V');
// DV1 = 11.5 V
let DV_2_3 = ltotal * R_2_3; // V
console.log('DV_2_3 =', DV_2_3, 'V');
// DV_2_3 = 8.049999999999999 V
console.log('DV_2_3 =', DV_2_3.toPrecision(3), 'V');
// DV_2_3 = 8.05 V
let DV4 = ltotal * R4; // V
console.log('DV4 =', DV4, 'V');
// DV4 = 40.25 V
console.log('DV4 =', DV4.toPrecision(3), 'V');
// DV4 = 40.3 V
DVtotal = DV1 + DV_2_3 + DV4; // V
console.log('DVtotal =', DVtotal, 'V');
// DVtotal = 59.8 V
console.log('DVtotal =', DVtotal.toPrecision(2), 'V');
// DVtotal = 60 V
```

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 75

---

## 9: Magnetism

---

### 9.01: Magnets and Magnetic Fields

---

![image_1](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_1.png)

![image_2](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_2.png)

![image_3](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_3.png)

![image_4](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_4.png)

![image_5](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_5.png)

![image_6](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_6.png)

![image_7](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_7.png)

![image_8](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_8.png)

![image_9](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_9.png)

![image_10](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_10.png)

![image_11](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_11.png)

![image_12](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_12.png)

![image_13](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_13.png)

![image_14](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_14.png)

![image_15](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_15.png)

![image_16](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_16.png)

![image_17](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_17.png)

![image_18](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_18.png)

![image_19](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_19.png)

![image_20](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_20.png)

![image_21](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_21.png)

![image_22](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_22.png)

![image_23](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_23.png)

![image_24](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_24.png)

![image_25](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_25.png)

![image_26](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_26.png)

![image_27](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_27.png)

![image_28](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_28.png)

![image_29](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_29.png)

![image_30](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_30.png)

![image_31](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_31.png)

---

1. A magnetic field of magnitude B = 0.10 T is directed perpendicular to a circular loop of wire of radius 0.22 m. Find the magnetic flux through the wire.

```js
let r = 0.22; // m
let B = 0.10; // T
let A = Math.PI * Math.pow(r, 2); // m^2
console.log('A =', A, 'm^2');
// A = 0.152053084433746 m^2
console.log('A =', A.toFixed(3), 'm^2');
// A = 0.152 m^2
let phi = B * A; // T * m^2
console.log('phi =', phi, 'T * m^2');
// phi = 0.0152053084433746 T * m^2
console.log('phi =', phi.toFixed(3), 'T * m^2');
// phi = 0.015 T * m^2
```

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 76

---

### 9.02: Forces in Magnetic Fields

---

![image_1](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_1.png)

![image_2](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_2.png)

![image_3](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_3.png)

![image_4](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_4.png)

![image_5](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_5.png)

![image_6](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_6.png)

![image_7](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_7.png)

![image_8](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_8.png)

![image_9](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_9.png)

![image_10](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_10.png)

![image_11](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_11.png)

![image_12](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_12.png)

![image_13](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_13.png)

![image_14](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_14.png)

![image_15](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_15.png)

![image_16](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_16.png)

![image_17](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_17.png)

![image_18](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_18.png)

![image_19](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_19.png)

![image_20](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_20.png)

![image_21](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_21.png)

![image_22](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_22.png)

![image_23](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_23.png)

![image_24](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_24.png)

![image_25](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_25.png)

![image_26](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_26.png)

![image_27](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_27.png)

![image_28](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_28.png)

![image_29](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_29.png)

---

1. A 6.0 m section of wire carries a current of 4.0 A from north to south. It is in a uniform magnetic field of 0.30 T pointing upward. What is the magnitude and direction of the magnetic force on the wire?

* You know the current I, the length L of the section of wire, and the magnetic field B, which enables you to calculate the magnitude of the magnetic force. You also know the direction of the current and the magnetic field and can use the right-hand rule to find the direction of the force.

```js
let I = 4.0; // A
let L = 6.0; // m
let B = 0.30; // T
FB = I * L * B; // N
console.log('FB =', FB, 'N');
// FB = 7.199999999999999 N
console.log('FB =', FB.toPrecision(2), 'N');
// FB = 7.2 N
```

* Find the direction of the force. Picture your right hand's fingers pointing in the direction of the magnetic field B upward and your thumb toward the current I to the south. The palm of your hand would then point west, so the force is toward the west.

---

2. A 6.0 m section of wire carries a current of 4.0 A from north to south. It is in a uniform magnetic field of 0.30 T pointing upward. What is the magnitude and direction of the magnetic force on the wire?

* You know the current I, the length L of the section of wire, and the magnetic field B, which enables you to calculate the magnitude of the magnetic force. You also know the direction of the current and the magnetic field and can use the right-hand rule to find the direction of the force.

```js
let I = 4.0; // A
let L = 6.0; // m
let B = 0.30; // T
FB = I * L * B; // N
console.log('FB =', FB, 'N');
// FB = 7.199999999999999 N
console.log('FB =', FB.toPrecision(2), 'N');
// FB = 7.2 N
```

* Picture your right hand's fingers pointing in the direction of the magnetic field B upward and your thumb toward the current I to the south. The palm of your hand would then point west, so the force is toward the west.

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 77

---

### 9.03: Electromagnetic Induction

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 78

---

## 10: Modern Physics

---

### 10.01: Atomic Spectra and Quantum Theory

---

### 10.02: The Nature of Light and the Photoelectric Effect

---

### 10.03: Relativity

---

### 10.04: Structure of the Nucleus

---

### 10.05: Radioactivity

---
