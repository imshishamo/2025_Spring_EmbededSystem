/* Core/Inc/usart.h */
#ifndef __USART_H__
#define __USART_H__

#include "stm32l4xx_hal.h"  // for UART_HandleTypeDef

extern UART_HandleTypeDef huart1;
void MX_USART1_UART_Init(void);

#endif /* __USART_H__ */
