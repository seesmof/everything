; .486    ; Use MPU coprocessor, maths with floating point numbers

.model small    ; Models can be: tiny, small, normal, large, huge, flat

sseg segment para stack 'stack'    ; sseg = keyword. Stack segment, beginning of stack declaration, third parameter can be: para / byte / word / dword, stack indicates that its a stack, 'stack' is a marker of the segment
    db 256 dup(?)  ; db = declare byte, 256 = times, dup = duplicate, (?) = no initial value. We take 256 1-byte segments without any initial values
sseg ends   ; End segment, like curly braces in higher level lanugages

; dseg, sseg, cseg are our own names that must be unique

dseg segment para public 'data' ; dseg = segment, para = paragraph, public = can access all data. Segment to access date in the program
    symbol db 'Y'   ; Declare A symbol
dseg ends ; End segment

cseg segment para public 'code' ; Declare code segment

    assume cs:cseg, ss:sseg, es:nothing    ; nothing = keyword. Here we declare that all those segments assosiate with 

start:  ; Declare procedure start that will call the main function. Entry point or a beginning of program execution
    ; Initialization of a data segment
    assume ds:dseg  ; Tells the assembler to use dseg segment for memory references using ds register
    mov bx,dseg     ; Copy DSEG to BX register
    mov ds,bx       ; Copy BX register into DS register

    call main   ; Call main function

    mov ah,04Ch ; 4C - function name to quit to OS. Exit to the OS
    mov al,0Fh  ; Exit code to ERRORLEVEL. Same as return 0
    int 21h     ; Interrupttion of DOS. A function set
    ; Add 0 at the beginning and h to the end so that they don't get confused with variable names. All HEX numbers we start with 0 and end with h

main proc near   ; proc = like func. Here we declare a function or a procedure called main
    xor ax,ax   ; AX <- 0

    mov dl,'*'  ; Any symbol to stdout

    mov ah,02h  ; ASCII to stdout
    int 21h     ;

    mov dl,symbol ; Symbol to stdout 

    mov ah,02h  
    int 21h

    mov dl,0Dh

    mov ah,02h
    int 21h

    mov dl,0Ah

    mov ah,02h
    int 21h

    ret ; End function execution and return to the place where it was called
main endp   ; End procedure or function

cseg ends   ; Close segment
end start   ; End program