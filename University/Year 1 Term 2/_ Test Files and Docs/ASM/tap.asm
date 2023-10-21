; .486    ; Use MPU coprocessor, maths with floating point numbers

.model small    ; Models can be: tiny, small, normal, large, huge, flat

sseg segment para stack 'stack'    ; sseg = keyword. Stack segment, beginning of stack declaration, third parameter can be: para / byte / word / dword, stack indicates that its a stack, 'stack' is a marker of the segment

    db 256 dup(?)  ; db = declare byte, 256 = times, dup = duplicate, (?) = no initial value. We take 256 1-byte segments without any initial values

sseg ends   ; End segment, like curly braces in higher level lanugages

dseg segment para public 'data' ; dseg = segment, para = paragraph, public = can access all data. Segment to access date in the program

; dseg, sseg, cseg are our own names that must be unique

    cats db 'A' ; Declare cats and assign A to it
    bats db 'B' ; Declare bats and assign B to it
    rats db 'C' ; Declare rats and assign C to it. To not assign any values use ? instead of data assigning

dseg ends ; End segment

cseg segment para public 'code' ; Declare code segment

    assume cs:cseg, ds:dseg, ss:sseg, es:nothing    ; nothing = keyword. Here we declare that all those segments assosiate with 

start proc far  ; Declare procedure start that will call the main function. Entry point or a beginning of program execution

    ; push ds     ; Save segment starting address to stack
    ; sub ax,ax   ; Substract AX register from AX or creating a 0 in AX register
    ; push ax     ; Save offset address to stack

    ; Initialization of a data segment
    mov bx,dseg ; Copy DSEG to BX register
    mov ds,bx   ; Copy BX register into DS register

    call main   ; Call main function
    ; ret         ; End function execution

    mov ah,04Ch ; 4C - function name to quit to OS. Exit to the OS
    mov al,0h   ; Exit code to ERRORLEVEL. Same as return 0
    int 21h     ; Interrupttion of DOS. A function set
    ; Add 0 at the beginning and h to the end so that they don't get confused with variable names. All HEX numbers we start with 0 and end with h

start endp  ; End procedure 

main proc near   ; proc = like func. Here we declare a function or a procedure called main

    mov ah,cats ; Copy cats to main function
    mov bh,bats ; Copy bats to main function
    mov ch,rats ; Copy rats to main function

    ret ; End function execution and return to the place where it was called

main endp   ; End procedure or function

cseg ends   ; Close segment
end start   ; End program