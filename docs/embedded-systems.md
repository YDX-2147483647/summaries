---
relevant:
  - ./digital-circuits-and-systems.md
  - ./operating-system.md
---

# 嵌入式系统原理与应用

!!! info "课程内容"

    本课基于 ARM v7 Cortex-A8。

    [网络教室](https://lexue.bit.edu.cn/course/view.php?id=12984)向所有同学开放——`justforfun`。

## 概述

### 嵌入式系统的处理器

> :material-clock-edit-outline: 2023年3月9日。

1. MCU: Micro controller unit.
2. DSP: Digital signal processor.
3. MPU: Micro processor unit.
4. SoC: System on a chip.

MCU 没有存储管理单元（memory management unit，MMU），一般无法安装 Linux；MPU 一般可以。

## ARM 处理器体系结构

### 工作模式与寄存器组

> :material-clock-edit-outline: 2023年3月9日，2023年3月10日，2023年3月13日。

<u>工作模式</u>如下。

- `usr` (user)（其余都是内核模式）
- `sys` (system)（其余内核模式都是异常模式）
- `svc` (supervisor)
- 中断相关：
  - `irq` (interrupt request)
  - `fiq` (Fast IRQ)
- 其它异常相关：
  - `abt` (abort)
  - `und` (undefined)
  - `mon` (secure monitor)

!!! info "优先级"

     除了`usr`、`sys`，所有模式都可由异常进入。这些异常按优先级从高到低如下。（此处优先数与优先级负相关）
     
     1. `svc`（复位）
     2. `abt`（data abort）
     3. `fiq`
     4. `irq`
     5. `und`（保护而不允许，prefetch abort）
     6. `svc`（正常调用子程序，software interrupt，SWI）、`und`（未定义或转给协处理器）

处理器有许多<u>通用寄存器</u>，但每种模式同时只用 16 个（R0–R15）。

- 前一半（R0–R7）所有模式通用。
- R8–R12 在 FIQ 专用，其余模式通用。
- R13 是 stack pointer（SP），用于函数调用、局部变量（堆栈指针）；R14 是 link register（LR），保存返回地址（断点地址）。这两个寄存器每种异常模式自己专用。
- R15 是 program counter（PC），记录程序当前运行的译码后的地址。

除了通用寄存器，还有<u>状态寄存器</u>，共用一个 current program status register（CPSR），6种异常模式各自专用 saved program status register（SPSR）。处理异常时，原来的 CPSR 会备份至 SPSR。

状态寄存器内容如下。

- 条件标志位（flag field）

  N（negative）、Z（zero）、C（carry）、V（overflow）。有许多指令会判断这些标志位。

- 控制位（control field）：

  - 中断屏蔽位 I（IRQ）、F（FIQ）可屏蔽所有来源的中断，处理异常时会用这两位实现优先级。
  - 状态控制位 T 表明处理器在 ARM 还是 Thumb 状态。（有多套指令集）
  - 模式控制位决定处理器的工作模式。虽只有 8 种模式，但用了 5 位。

- ……

### 存储数据

> :material-clock-edit-outline: 2023年3月9日。

“低地址⇔低位”则称作小端（little-endian）模式，否则称作大端。

为了方便寻址，存储时对齐数据。具体方式如下。（以`struct`为例）

!!! note "不一定要对齐"

    ARM 也支持不对齐，但那样地址必然增加位数，仍会牺牲效率。

1. 按声明顺序依次处理每项数据。
   1. 存储本项数据：`char` ↦ 1 B，`short` ↦ 2 B，……（按大／小端）
   2. 必要时空出一些位置，保证下一项数据对齐。（首地址是所占空间的整倍数）
2. 必要时空出一些位置，保证按数组存储时下一项也能对齐。（所占空间是最长数据的整倍数）

```rust
use std::mem;

#[repr(C)]
struct FieldStruct {
    first: u8,
    second: u16,
    third: u8
}

// The size of the first field is 1, so add 1 to the size. Size is 1.
// The alignment of the second field is 2, so add 1 to the size for padding. Size is 2.
// The size of the second field is 2, so add 2 to the size. Size is 4.
// The alignment of the third field is 1, so add 0 to the size for padding. Size is 4.
// The size of the third field is 1, so add 1 to the size. Size is 5.
// Finally, the alignment of the struct is 2 (because the largest alignment amongst its
// fields is 2), so add 1 to the size for padding. Size is 6.
assert_eq!(6, mem::size_of::<FieldStruct>());
```

!!! tip "🦀 Rust"

    数据对齐部分参考了 [Rust Doc](https://doc.rust-lang.org/std/mem/fn.size_of.html#size-of-reprc-items)。

## ARM 指令集

### 指令

> :material-clock-edit-outline: 2023年3月13日。
>
> :material-eye-arrow-right: [ARM Compiler armasm User Guide](https://developer.arm.com/documentation/dui0473/m/arm-and-thumb-instructions/arm-and-thumb-instruction-summary).

- **跳转**（B, BL, BX, BLX）

  - B: Branch.
  - –L: …with link (set [R14 link register](#工作模式与寄存器组)).
  - –X: …change instruction set (ARM / Thumb).

- **处理数据**

  - **复制**

    - MOV: Move.

    - MVN: Move not.

  - **算术**（ADD, ADC; SUB, SBC, RSB, RSC）

    - ADD, AD–: Add.
    - SUB, SB–, –S–: Subtract.
    - R–: Reverse…
    - –C: …with carry (from flag field).

  - **位、逻辑**

    - AND: Logical and.
    - ORR: Logical or.
    - EOR: Exclusive or.
    - BIC: Bit clear.

  - **比较**

    这些指令只设置标志位，中间结果不存储到通用寄存器。

    - CMP: Compare.
    - CMN: Compare negative (sum).
    - TST: Test.
    - TEQ: Test equivalence.

- **状态寄存器**

  - MRS: Move from PSR / system coprocessor to register.
  - MSR: Move from register to PSR / system coprocessor.

- **存储器**（LDR, LDM; STR, STM; SWP）

  ```mermaid
  flowchart LR
      Rn[Rn<br><small>address base</small>] -.-> memory
      Rt[Rt<br><small>target</small>]
      Rt -->|"STR Rt, [Rn]"| memory([memory])
      memory -->|"LDR Rt, [Rn]"| Rt
  ```

  - LDR, LD–: load register with word.

  - STR, ST–: Store register with word.

  - [–M](https://developer.arm.com/documentation/dui0473/m/arm-and-thumb-instructions/stm): …multiple registers.

    !!! note "顺序"

        `LDR Rt, [Rn]`，但是`LDM Rn, {Rt, …}`。

    - Address mode

      - I– / D–: Increase / decrease address…
      - –A / – B: …after / before each transfer.

      IA is the default.

      PUSH = STMDB, POP = LDMIA.

      [Alternatively](https://developer.arm.com/documentation/ddi0597/2022-12/Base-Instructions/STMDA--STMED--Store-Multiple-Decrement-After--Empty-Descending--),

      - F– / E–: Full / empty… (equivalent to –B / –A)
      - –A / –D: …ascending / descending stack. (equivalent to I– / D–)

      !!! info "Full / empty stack"

          In an empty stack, the stack pointer points to the next empty location on the stack. In a full stack, it points to the top-most item.

  - `!` is an optional suffix for the address register. If present, the final address is written back into base register.

    !!! info "[Addressing modes](https://developer.arm.com/documentation/den0042/a/Unified-Assembly-Language-Instructions/Memory-instructions/Addressing-modes)"

        | Instruction          | Addressing mode | Address | Write back               |
        | -------------------- | --------------- | ------- | ------------------------ |
        | `LDR R0, [R1]`       | Register        | R1      | ✗                        |
        | `LDR R0, [R1, #2]`   | Pre-indexed     | R1 + 2  | ✗                        |
        | `LDR R0, [R1, #2]!`  | Pre-indexed     | R1 + 2  | R1 ≔ R1 + 2              |
        | `LDR R0, [R1], #2`   | Post-indexed    | R1      | R1 ≔ R1 + 2              |
        | `LDMIA R1!, {R2-R7}` | Pre-indexed     | R1      | R1 ≔ R1 + 1 (many times) |
        
        Additionally, the offset (`#2` here) can also be `R2` or `R2, LSL #3` (R2 × 2³).
  
  - SWP: Swap between registers and memory. (deprecated in ARMv6 and above)
  
    ```assembly
    LDR <destination>, <source>, [<address>]
    ```
  
    ```mermaid
    flowchart LR
        source[Rt2<br><small>source</small>] --> memory([memory]) --> destination[Rt1<br><small>destination</small>]
        address[Rn<br><small>address base</small>] -.-> memory
    ```
  
    source ≠ address ≠ destination. (source can be the same register as destination.)
  

# 后备箱

- 十六进制最大数码是 F（15）。
