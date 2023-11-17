; Define the model as small
.model small

; Define the stack segment
sseg segment para stack 'stack'
db 256 dup(?)
sseg ends

; Define the data segment
dseg segment para public 'data'
; Define the variable 'cats'
cats db 'A'
; Define the variable 'bats'
bats db 'B'
; Define the variable 'rats'
rats db 'C'
dseg ends

; Define the code segment
cseg segment para public 'code'
; Set the segment registers
assume cs:cseg, ds:dseg, ss:sseg, es:nothing

; Define the start procedure
start proc far
; Move the value of the data segment to the BX register
mov bx,dseg
; Move the value of the BX register to the DS register
mov ds,bx
; Call the main procedure
call main
; Set the exit code to 0
mov ah,04Ch
mov al,0h
int 21h
; End the start procedure
start endp

; Define the main procedure
main proc near
; Move the value of 'cats' into the AH register
mov ah,cats
; Move the value of 'bats' into the BH register
mov bh,bats
; Move the value of 'rats' into the CH register
mov ch,rats
; Return from the procedure
ret
; End the main procedure
main endp

; End the code segment
cseg ends
; End the program
end start
