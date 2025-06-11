/* Core/Inc/hc_sr505.h */
#ifndef __HC_SR505_H_
#define __HC_SR505_H_

#include <stdint.h>  // for uint8_t

typedef enum
{
    manned = 0,
    unmanned
} IsThereAnyone;

uint8_t hs_sr505_Judge(void);
void PrintfDebug(const char *fmt, ...);

#endif /* __HC_SR505_H_ */
