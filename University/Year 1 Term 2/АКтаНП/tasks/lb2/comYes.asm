.model tiny     ; set program model as tiny

cseg segment para public 'code'     ; Declare code segment
    assume cs:cseg, ds:cseg, ss:cseg, es:nothing    ; set each code segment to code seg as it is the only segment in the program 
    org 100h    ; start loading the first instruction at 100h

start:  ; declare program entry point
    call main   ; call main function

    mov ah, 04Ch    ; exit to OS
    mov bl, 6Ch     ; set error code to 108 in hex 
    int 21h     ; call interrupt
    
    symbol db 'U'   ; declare a symbol to output

main proc near  ; declare main procedure
    call newline    ; call newline function
    
    xor ax, ax   ; clear ax register
    mov dl, symbol      ; load symbol to stdout 
    mov ah, 02h     ; output symbol to stdout
    int 21h     ; call interrupt

    mov dl, 'k'     ; load symbol to stdout
    mov ah, 02h     ; output symbol to stdout
    int 21h     ; call interrupt
 
    mov dl, 'r'     ; load symbol to stdout
    mov ah, 02h     ; output symbol to stdout
    int 21h     ; call interrupt

    mov dl, 'a'     ; load symbol to stdout
    mov ah, 02h     ; output symbol to stdout
    int 21h     ; call interrupt

    mov dl, 'i'     ; load symbol to stdout
    mov ah, 02h     ; output symbol to stdout
    int 21h     ; call interrupt

    mov dl, 'n'     ; load symbol to stdout
    mov ah, 02h     ; output symbol to stdout
    int 21h     ; call interrupt

    mov dl, 'e'     ; load symbol to stdout
    mov ah, 02h     ; output symbol to stdout
    int 21h     ; call interrupt

    call newline    ; call newline function

    mov dl, '<'     ; load symbol to stdout
    mov ah, 02h     ; output symbol to stdout
    int 21h     ; call interrupt

    mov dl, '3'     ; load symbol to stdout
    mov ah, 02h     ; output symbol to stdout
    int 21h     ; call interrupt

    call newline    ; call newline function

    ret ; end function execution
main endp   ; end procedure

newline proc near   ; declare modular procedure
    mov dl, 10      ; set dl register to new line
    mov ah, 02h     ; output it to stdout
    int 21h     ; call interrupt
    mov dl, 13      ; set dl register to carret return
    mov ah, 02h     ; output it to stdout
    int 21h     ; call interrupt

    ret ; end function execution
newline endp    ; end procedure
    

cseg ends   ; close segment
end start   ; end program execution