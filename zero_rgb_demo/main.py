import array, time
from machine import Pin
import rp2
from rp2 import PIO, StateMachine, asm_pio

@asm_pio(sideset_init=PIO.OUT_LOW, out_shiftdir=PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    label("bitloop")
    out(x, 1)               .side(0)    [T3 - 1] 
    jmp(not_x, "do_zero")   .side(1)    [T1 - 1] 
    jmp("bitloop")          .side(1)    [T2 - 1] 
    label("do_zero")
    nop()                   .side(0)    [T2 - 1]
    
# Create the StateMachine with the ws2812 program, outputting on Pin(16).
sm = StateMachine(0, ws2812, freq=8000000, sideset_base=Pin(16))

# Start the StateMachine, it will wait for data on its FIFO.
sm.active(1)

# Define some LED RGB colors.
colors = {
    #           red<<16 ,   green<<8, blue
    "white":  ( (200<<16) | (200<<8) | 200 ),
    "yellow": ( (150<<16) | ( 70<<8) |   0 ),
    "orange": ( (190<<16) | ( 22<<8) |   0 ),
    "red":    ( (200<<16) | (  0<<8) |   0 ),
    "purple": ( (200<<16) | (  0<<8) | 160 ),
    "blue":   ( (  0<<16) | (  0<<8) | 200 ),
    "green":  ( (  0<<16) | (180<<8) |   0 ),
    "lime":   ( ( 40<<16) | ( 80<<8) |  10 ),
    "off":    (    0<<16  | (  0<<8) |   0 )
    }

print("white")
sm.put(colors["white"],8) 
time.sleep_ms(2000)
sm.put(colors["off"],8) 
time.sleep_ms(200)

print("yellow")
sm.put(colors["yellow"],8) 
time.sleep_ms(2000)
sm.put(colors["off"],8) 
time.sleep_ms(200)

print("orange")
sm.put(colors["orange"],8) 
time.sleep_ms(2000)
sm.put(colors["off"],8) 
time.sleep_ms(200)

print("red")
sm.put(colors["red"],8) 
time.sleep_ms(2000)
sm.put(colors["off"],8) 
time.sleep_ms(200)

print("purple")
sm.put(colors["purple"],8) 
time.sleep_ms(2000)
sm.put(colors["off"],8) 
time.sleep_ms(200)

print("blue")
sm.put(colors["blue"],8) 
time.sleep_ms(2000)
sm.put(colors["off"],8) 
time.sleep_ms(200)

print("green")
sm.put(colors["green"],8) 
time.sleep_ms(2000)
sm.put(colors["off"],8) 
time.sleep_ms(200)  
    
print("lime")
sm.put(colors["lime"],8) 
time.sleep_ms(2000)
sm.put(colors["off"],8) 
time.sleep_ms(200)       