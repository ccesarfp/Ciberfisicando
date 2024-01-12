# direct-mapped-cache-original

<details open>
<summary>Português</summary>
Implementação de um modelo de memória cache por meio de Mapeamento Direto.

## Objetivo
Este repositório contém a implementação em Python de um modelo de memória cache por mapeamento direto, originalmente desenvolvido como parte de um desafio em uma disciplina de Performance de Sistemas. 

## Funcionamento do Modelo de Memória Cache

### Especificações

- Capacidade da memória principal: 2048 palavras
- Capacidade total da memória cache: 128 palavras
- Tamanho da cache line: 16 palavras

### Endereçamento
Os endereços gerados pela CPU são divididos nos seguintes blocos de bits:

- w: especifica uma das K palavras de uma cache line ou bloco de memória.
- r: especifica o índice do cache line.
- t: etiqueta (tag) que identifica o bloco de memória principal atualmente armazenado naquela cache line.
- s: concatenação dos bits de t e r, representando o número do bloco de memória principal onde está a palavra desejada.

### Algoritmo
1. Ao receber a solicitação de uma palavra de memória em um endereço x, extrai-se r e t de x.
2. Verifica-se se t é igual ao tag t' contido na linha r da cache line.
- Se houver um "cache hit," retorna a palavra na posição w dos dados da cache line.
- Se ocorrer um "cache miss," continua para o próximo passo.
3. Se a cache line r foi alterada, ela é copiada para a memória principal.
4. O bloco s da memória principal é trazido para a cache line, e a palavra no endereço solicitado é retornada à CPU.

</details>

<details>
<summary>English</summary>
Implementation of a cache memory model through Direct Mapping.
  
## Goal

This repository contains the Python implementation of a direct-mapped cache memory model, originally developed as part of a challenge in a Systems Performance course.

## Operation of the Cache Memory Model

### Specifications
- Main memory capacity: 2048 words
- Total cache memory capacity: 128 words
- Cache line size: 16 words

### Addressing
CPU-generated addresses are divided into the following bit blocks:

- w: specifies one of the K words in a cache line or memory block.
- r: specifies the index of the cache line.
- t: tag that identifies the memory block currently stored in that cache line.
- s: concatenation of t and r bits, representing the main memory block number where the desired word is located.

### Algorithm
1. Upon receiving a memory word request at address x, extract r and t from x.
2. Check if t is equal to the tag t' contained in line r of the cache line.
- If a "cache hit" occurs, return the word at position w in the cache line data.
- If a "cache miss" occurs, proceed to the next step.
4. If cache line r has been modified, copy it to main memory.
5. Block s from main memory is brought into the cache line, and the word at the requested address is returned to the CPU.
</details>
