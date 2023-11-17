.model tiny    ; Models can be: tiny, small, normal, large, huge, flat

cseg segment para public 'code' ; Declare code segment
    assume cs:cseg, ds:cseg, ss:cseg, es:nothing    ; nothing = keyword. Here we declare that all those segments assosiate with 
    org 100h

start:  ; Declare procedure start that will call the main function. Entry point or a beginning of program execution
    call main   ; Call main function

    mov ah,04Ch ; 4C - function name to quit to OS. Exit to the OS
    mov al,6Ch ; Exit code to ERRORLEVEL. Same as return 0
    int 21h     ; Interrupttion of DOS. A function set
    ; Add 0 at the beginning and h to the end so that they don't get confused with variable names. All HEX numbers we start with 0 and end with h
    
    symbol db 'U'   ; Declare A symbol

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