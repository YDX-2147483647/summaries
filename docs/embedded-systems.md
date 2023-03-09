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

> :material-clock-edit-outline: 2023年3月9日。

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

处理器有许多<u>通用寄存器</u>，但每种模式同时只用 16 个（R0–R15）。

- 前一半（R0–R7）所有模式通用。
- R8–R12 在 FIQ 专用，其余模式通用。
- R13 是 stack pointer（SP），用于函数调用、局部变量；R14 是 link register（LR），保存返回地址。这两个寄存器每种异常模式自己专用。
- R15 是 program counter（PC），记录程序当前运行的译码后的地址。

除了通用寄存器，还有<u>状态寄存器</u>，共用一个 current program status register（CPSR），6种异常模式各自专用 saved program status register（SPSR）。状态寄存器内容如下。

- 条件标志位

  N（negative）、Z（zero）、C（carry）、V（overflow）。有许多指令会判断这些标志位。

- 控制位：

  - 中断屏蔽位 I（IRQ）、F（FIQ）可屏蔽所有中断。
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
