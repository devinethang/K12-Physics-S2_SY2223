# K12-Physics-S2_SY2223

A collection of formulas for Physics calculations

* Hardcover - [Physics: Problems and Solutions](https://www.amazon.com/gp/product/1601530552/)

## References

* [Mathematics in R Markdown](https://rpruim.github.io/s341/S19/from-class/MathinRmd.html)

## 1: Momentum

### 1.01: Semester Introduction

![image_1](1%20-%20Momentum/1-01%20-%20Semester%20Introduction/image_1.png)

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

### 1.08: Conservation of Angular Momentum

![image_1](1%20-%20Momentum/1-08%20-%20Conservation%20of%20Angular%20Momentum/image_1.png)

![image_2](1%20-%20Momentum/1-08%20-%20Conservation%20of%20Angular%20Momentum/image_2.png)

![image_3](1%20-%20Momentum/1-08%20-%20Conservation%20of%20Angular%20Momentum/image_3.png)

![image_4](1%20-%20Momentum/1-08%20-%20Conservation%20of%20Angular%20Momentum/image_4.png)

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

## 2: Work

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

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 44

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
