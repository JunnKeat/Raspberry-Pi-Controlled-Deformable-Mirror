from ServoPi import PWM

pwm = PWM(0x40)
pwm.set_pwm_freq(200)
pwm.output_enable()
pwm.set_pwm(1,0,3000)
