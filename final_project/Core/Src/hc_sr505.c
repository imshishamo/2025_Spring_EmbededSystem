/* Core/Src/hc_sr505.c */
#include "hc_sr505.h"
#include "stm32l4xx_hal.h"  // HAL GPIO 必要定義
#include "usart.h"          // PrintfDebug 需要用到 huart1
#include <stdarg.h>
#include <stdio.h>

/* 讀 GPIOA PA0 判斷 SR505 */
uint8_t hs_sr505_Judge(void)
{
    if ((GPIOA->IDR & GPIO_PIN_0) == GPIO_PIN_0)
    {
        return manned;
    }
    else
    {
        return unmanned;
    }
}

/* 自己實作 printf 送到 UART1 */
void PrintfDebug(const char *fmt, ...)
{
    char Uart_buf[128];
    va_list args;
    va_start(args, fmt);
    int length = vsnprintf(Uart_buf, sizeof(Uart_buf) - 1, fmt, args);
    va_end(args);
    HAL_UART_Transmit(&huart1, (uint8_t *)Uart_buf, length, HAL_MAX_DELAY);
}
