---
## Basic Information

| Exchange | Stands For                                              | Common Use-Cases                                    |
|:--------:|:--------------------------------------------------------|:----------------------------------------------------|
| **NASDAQ** | National Association of Securities Dealers Automated Quotations | Tech- and growth-company listings; high-volume electronic trading |
| **NYSE**   | New York Stock Exchange                                 | Large-cap and blue-chip listings; benchmark price discovery |
| **BATS**   | Better Alternative Trading System (now part of Cboe)     | Low-fee alternative for equities; high-speed institutional order flow |
| **ARCA**   | Originally “Archipelago Exchange,” now NYSE Arca         | Very active ETF execution; electronic equity trading |

---

## 1. Financial Perspective  
Focus: market model, listing standards, liquidity, and trading mechanisms.

| Exchange   | Market Model                    | Listings & Sectors                            | Typical Spread & Liquidity¹ |
|:----------:|:--------------------------------|:-----------------------------------------------|:----------------------------|
| **NASDAQ** | Dealer (multiple market makers) | Tech-heavy; younger growth companies           | Narrow spreads in tech; deep order books |
| **NYSE**   | Auction (single specialist)     | Large-cap, established firms across sectors    | Ultra-tight spreads; extreme depth |
| **BATS**   | Electronic matching             | Broad-market equities; institutional order flow| Often lowest fees → tight spreads |
| **ARCA**   | Fully electronic                | ETFs & highly liquid equities                  | Excellent for ETF execution; minimal latency |

¹ Spreads and liquidity vary intraday; these are typical qualitative patterns.

- **NASDAQ vs. NYSE**  
  - **NASDAQ** operates as a *dealer market*: designated Market Makers post bid/ask quotes and trade from inventory.  
  - **NYSE** uses a *continuous auction*: a single Designated Market Maker (DMM) matches buy/sell orders on a central limit order book.

- **BATS & ARCA**  
  - Both are *alternative trading systems* with purely electronic matching engines, competing on ultra-low latency and fee structures to attract high-volume order flow.

---

## 2. Scientific/Technological Perspective  
Focus: network architecture, matching engines, and performance characteristics.

- **Matching Engine**  
  - All four use central limit order books (CLOB) but differ in implementation:  
    - **NYSE Arca & BATS**: Highly parallelized C++/Java engines optimized for >1 million messages/sec.  
    - **NASDAQ**: Proprietary engine with distributed matching across multiple data centers.

- **Latency & Throughput**  
  $$
    L_{\text{avg}} \approx
    \begin{cases}
      50–100\ \mu\mathrm{s}, & \text{(BATS, ARCA)}\\
      150–250\ \mu\mathrm{s}, & \text{(NASDAQ, NYSE)}
    \end{cases}
    ,\quad
    T \sim 10^6\ \text{msg/s}
  $$

- **Network Topology**  
  - **Co-location** in key data centers (e.g., Mahwah, NJ) to minimize propagation delay.  
  - **Multicast market-data feeds** broadcast order-book updates at microsecond resolution.

---

## 3. Mathematical Perspective  
Focus: order-flow modeling, matching algorithms, and queue dynamics.

1. **Order-Book State**  
   $$
     B = \{(p_i, q_i)\}_{i=1}^m,\quad
     A = \{(p_j, q_j)\}_{j=1}^n
   $$
   where \(p_i\)=price level, \(q_i\)=queued quantity.

2. **Matching Rule (Price–Time Priority)**  
   - **Price priority**: match highest bid \(p_b\) with lowest ask \(p_a\) if \(p_b \ge p_a\).  
   - **Time priority**: FIFO within same price level.

3. **Stochastic Arrival Model**  
   - Limit orders arrive as Poisson processes with rates \(\lambda_b\) (bids/sec) and \(\lambda_a\) (asks/sec).  
   - **Expected queue length** at best bid (M/M/1 approx):  
     $$
       E[Q] = \frac{\lambda_b}{\mu_b - \lambda_b},
     $$
     where \(\mu_b\) is the matching (service) rate.

4. **Execution Probability**  
   - For a small market order of size \(x\):  
     $$
       P(\text{exec} \mid x)
       = 1 - \sum_{k=0}^{x-1} \frac{\bar Q^k e^{-\bar Q}}{k!},
       \quad \bar Q = E[Q].
     $$

5. **Latency’s Role in Adverse Selection**  
   - Let \(\Delta t\) = observer’s latency.  
   - Adverse selection cost scales roughly as:  
     $$
       C_{\text{adv}} \propto \lambda_{\text{informed}}\cdot \Delta t.
     $$
   - Exchanges with lower \(\Delta t\) (BATS/ARCA) reduce this cost.

---

**Bottom Line:**  
- **Basic:** NASDAQ and NYSE are the two legacy U.S. exchanges (dealer vs. auction), BATS and ARCA are fast, fee-competitive alternatives.  
- **Financially:** they differ in market‐making model, listing profiles, and liquidity characteristics.  
- **Technically:** all leverage ultra-low-latency, high-throughput engines and co-located networks, with BATS/ARCA typically the fastest.  
- **Mathematically:** their behavior can be captured via queueing theory, Poisson order arrival, and latency-driven execution risk.
