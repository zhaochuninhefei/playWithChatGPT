在ChatGPT帮助下写代码的一次尝试
=====

# 一、背景

去年12月开始调戏ChatGPT，越调戏越心寒，被它的语言理解能力震撼，直观上目前就已经能很有效地提升程序员的开发效率，以后能迭代到什么样子，会不会导致程序员失业，这些问题越想越害怕。

但害怕没有用，程序员必须拥抱变化，所以先尝试真的用它来做开发，看看效果怎么样。

目前chatGPT对自己的定位是助手，这个定位目前来说很准确，今天就把它当成助手，来尝试写点代码。

正好今天需要用go实现一个位图功能，也不去找轮子了，就自己造一个，在chatGPT的帮助下。。。

# 二、与ChatGPT交流过程
这里直接给出与ChatGPT的交流过程：

## 问题1

**我的提问:** `如何用go定义一个位图?`

**chatGPT的回答:**

在Go中，可以使用 `[]bool` 类型来表示位图。但是，由于 `bool` 类型需要占用一个字节，因此如果需要处理大量的位，使用 `[]bool` 可能会占用大量的内存。因此，使用 `[]byte` 类型来表示位图更加常见，因为它可以有效地存储单个位。

下面是使用 `[]byte` 定义一个位图的示例：
```go
type BitMap []byte

// 将位图中指定的位置设置为 1
func (bitmap BitMap) SetBit(pos int) {
    index := pos / 8
    offset := uint(pos % 8)
    bitmap[index] |= 1 << offset
}

// 将位图中指定的位置设置为 0
func (bitmap BitMap) ClearBit(pos int) {
    index := pos / 8
    offset := uint(pos % 8)
    bitmap[index] &= ^(1 << offset)
}

// 检查位图中指定的位置是否为 1
func (bitmap BitMap) CheckBit(pos int) bool {
    index := pos / 8
    offset := uint(pos % 8)
    return (bitmap[index] & (1 << offset)) != 0
}

```
在这个示例中，我们使用 []byte 类型定义了一个 BitMap 类型。它提供了三个方法：

- `SetBit(pos int)` 将指定位置设置为 1。
- `ClearBit(pos int)` 将指定位置设置为 0。
- `CheckBit(pos int) bool` 检查指定位置是否为 1。

在这些方法中，我们使用 `pos` 参数表示位图中的位置，将它转换为 `index` 和 `offset`，其中 `index` 表示位图中的字节索引，`offset` 表示该字节中的位偏移量。在 `SetBit` 方法中，我们使用位运算符 `|=` 将指定位置设置为 `1`。在 `ClearBit` 方法中，我们使用位运算符 `&^=` 将指定位置设置为 `0`。在 `CheckBit` 方法中，我们使用位运算符 `&` 和位移运算符 `<<` 来检查指定位置是否为 `1`。

这只是一个简单的实现示例，实际上位图的实现可能更加复杂，需要根据实际情况进行优化。

> **我的考虑:** 这个回答不是很符合我的要求，我想要一个直接用int实现的位图，所以需要继续提问。

## 问题2

**我的提问:** `使用go语言实现一个位图，并提供它和int之间的转换`

**chatGPT的回答:**

在Go语言中，我们可以使用一个无符号整数作为位图。例如，如果需要表示一个长度为8的位图，可以使用一个 uint8 类型的变量。同样，如果需要表示一个长度为32的位图，可以使用一个 uint32 类型的变量。以下是一个示例实现：
```go
package main

import (
    "fmt"
)

// BitSet 代表一个位图
type BitSet uint32

// SetBit 将位图中第 i 位设置为 1
func (b *BitSet) SetBit(i uint) {
    mask := uint32(1) << (i % 32)
    (*b) |= BitSet(mask)
}

// ClearBit 将位图中第 i 位设置为 0
func (b *BitSet) ClearBit(i uint) {
    mask := uint32(1) << (i % 32)
    (*b) &= BitSet(^mask)
}

// TestBit 检查位图中第 i 位是否为 1
func (b *BitSet) TestBit(i uint) bool {
    mask := uint32(1) << (i % 32)
    return ((*b) & BitSet(mask)) != 0
}

// ToInt 将位图转换为一个整数
func (b *BitSet) ToInt() int {
    return int(*b)
}

// FromInt 将一个整数转换为位图
func FromInt(i int) BitSet {
    return BitSet(i)
}

func main() {
    var b BitSet
    b.SetBit(3)
    b.SetBit(7)
    fmt.Printf("%032b\n", b.ToInt())

    b.ClearBit(3)
    fmt.Printf("%032b\n", b.ToInt())

    fmt.Println(b.TestBit(3))
    fmt.Println(b.TestBit(7))

    var i int = 255
    b = FromInt(i)
    fmt.Printf("%032b\n", b.ToInt())
}

```
在这个示例中，我们定义了一个 BitSet 类型，它是一个 uint32 的别名。我们提供了三个方法来操作位图：SetBit、ClearBit 和 TestBit。其中，SetBit 和 ClearBit 用于设置和清除位图中的某一位，而 TestBit 用于检查某一位是否为 1。我们还提供了两个方法来进行位图和整数之间的转换：ToInt 将位图转换为一个整数，FromInt 将一个整数转换为位图。

> **我的考虑:** 其实我的第二个问题没有清楚地表述出我想直接用int实现位图的意图，但chatGPT依然给出了我想要的代码原型，这个代码原型的完成度已经很高了，可以直接运行，作为示例完全没有问题了。当然为了使用方便，我们还需要一个位图与二进制字符串之间转换的功能，这个问题简单，但我仍然问了chatGPT问题3，看看它如何回答。

## 问题3

**我的提问:** `使用go语言实现uint和二进制字符串之间的转换`

**chatGPT的回答:**

可以使用内置的 strconv 包中的 FormatUint 和 ParseUint 函数来实现 uint 和二进制字符串之间的转换。

下面是一个将 uint 转换为二进制字符串的示例：
```go
package main

import (
    "fmt"
    "strconv"
)

func main() {
    var x uint = 42
    binaryStr := strconv.FormatUint(uint64(x), 2)
    fmt.Println(binaryStr)
}

```
输出：
```
101010
```
其中 strconv.FormatUint 的第一个参数是需要转换的 uint，第二个参数是进制，这里是二进制，所以为 2。

下面是一个将二进制字符串转换为 uint 的示例：
```go
package main

import (
    "fmt"
    "strconv"
)

func main() {
    binaryStr := "101010"
    x, _ := strconv.ParseUint(binaryStr, 2, 0)
    fmt.Println(x)
}

```
输出：
```
42
```
其中 strconv.ParseUint 的第一个参数是需要转换的字符串，第二个参数是进制，这里是二进制，所以为 2。第三个参数是指定转换的结果类型的位数，这里设置为 0，表示根据输入字符串自动选择合适的位数。

> **我的考虑:** 很详细的回答，无话可说。。。

# 三、完成功能开发
在与chatGPT交流之后，基于它给出的代码原型，很快就写出了go的位图实现包，具体代码可以参考我的开源项目:

<a href="https://github.com/zhaochuninhefei/zcutils-go/blob/main/zcbitmap/zcbitmap.go" target="_blank">github的zcbitmap</a>

<a href="https://gitee.com/zhaochuninhefei/zcutils-go/blob/main/zcbitmap/zcbitmap.go" target="_blank">gitee的zcbitmap</a>

# 四、感想
目前的ChatGPT，将它作为程序员的助手，只要你的问题足够具体清晰，那么它可以很好很高效地回答并给出高质量的代码原型。不用chatGPT当然也能做出来，但自己思考或基于当下的搜索引擎查找资料，再写出代码原型的话，效率上肯定是要慢很多的。

当然，目前它的回答你也不能完全相信，需要验证一下，比如之前有一次我问它`65536 / 1024 等于多少`，它一会回答`128`，一会回答`32`。。。还说自己擅长计算，就挺欢乐的。。。

总的来说，目前感想：

1. 需求分解的越细致，chatGPT的回答质量越高，但如何提出高效的问题，即如何将一个需求分解为足够细致的问题向chatGPT提出，也是有一些讲究的。
2. 如果需求是一个需要完全创新的课题的话，目前的chatGPT能否给出高质量的回答还是存疑的。
3. 目前chatGPT还是不能取代程序员的，只能作为助手使用，而且它的回答需要验证。

至于以后这货会不会迭代到能基本代替程序员，各个大厂能不能把类似的模型搞起来并且相对便宜地提供服务，会不会导致程序员大面积失业去抢别人饭碗。。。谁知道呢。。。
