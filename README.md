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
let QheatIce = 100 * 2.05 / 1000 * 100; // kJ
console.log('QheatIce =', QheatIce, 'kJ');
// QheatIce = 20.499999999999996 kJ
console.log('QheatIce =', QheatIce.toPrecision(3), 'kJ');
// QheatIce = 20.5 kJ
```

Ice melting at 0°C

`q = m * DHf`

```js
let m = 100; // g
let QiceMelt = 100 * 334 / 1000; // kJ
console.log('QiceMelt =', QiceMelt, 'kJ');
// QiceMelt = 33.4 kJ
```

Heating liquid water from 0°C to 100°C

`q = m * C * DT`

```js
let m = 100; // g
let QheatWater = 100 * 4.18 / 10; // kJ
console.log('QheatWater =', QheatWater, 'kJ');
// QheatWater = 41.8 kJ
```

Liquid water boiling at 100°C

`q = m * DHf`

```js
let m = 100; // g
let QboilWater = 100 * 2.26; // kJ
console.log('QboilWater =', QboilWater, 'kJ');
// QboilWater = 225.99999999999997 kJ
console.log('QboilWater =', Math.round(QboilWater), 'kJ');
// QboilWater = 226 kJ
```

Heating steam from 100°C to 200°C

`q = m * C * DT`

```js
let m = 100; // g
let QheatSteam = 100 * 2.08 / 10; // kJ
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
