	.file	"sigsegv.c"
	.section	.rodata
.LC0:
	.string	"caught SIGSEGV"
	.text
	.globl	sigsegvHandler
	.type	sigsegvHandler, @function
sigsegvHandler:
.LFB2:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$16, %rsp
	movl	%edi, -4(%rbp)
	movl	$.LC0, %edi
	call	puts
	nop
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE2:
	.size	sigsegvHandler, .-sigsegvHandler
	.section	.rodata
.LC1:
	.string	"signal()"
	.text
	.globl	main
	.type	main, @function
main:
.LFB3:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$16, %rsp
	movl	$sigsegvHandler, %esi
	movl	$11, %edi
	call	signal
	cmpq	$-1, %rax
	jne	.L4
	movl	$.LC1, %edi
	call	perror
	movl	$2, %edi
	call	exit
.L4:
	movq	$26292537, -8(%rbp)
	movq	-8(%rbp), %rax
	leaq	4(%rax), %rdx
	movq	%rdx, -8(%rbp)
	movl	(%rax), %eax
	movl	%eax, -12(%rbp)
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE3:
	.size	main, .-main
	.ident	"GCC: (GNU) 4.8.3 20140911 (Red Hat 4.8.3-7)"
	.section	.note.GNU-stack,"",@progbits
