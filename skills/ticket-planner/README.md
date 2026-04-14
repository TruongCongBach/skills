# Ticket Planner

`ticket-planner` dùng sau `ticket-analysis`, trước khi bắt đầu code.

## Dùng khi nào

- Khi ticket đã đủ rõ và bạn cần chọn hướng implement
- Khi cần compare 1-2 hướng fix hoặc feature approach
- Khi cần affected areas, risks, edge cases, test plan trước khi code

## Không dùng khi nào

- Khi ticket còn mơ hồ, chưa rõ vấn đề
- Khi bạn đã quyết định plan và đang bước vào implement
- Khi bạn chỉ cần review code đã viết

## Mục tiêu

- Chuyển kết quả analysis thành plan thực thi
- Đề xuất approach A/B nếu cần
- Chỉ ra module/file/area có khả năng bị ảnh hưởng
- Nêu risks, tradeoffs, state handling, API dependencies

## Input thường gặp

- Output từ `ticket-analysis`
- Jira ticket
- Screenshot/log bổ sung nếu ảnh hưởng tới plan

## Output mong đợi

- Proposed approach A
- Proposed approach B nếu relevant
- Recommended approach
- Affected areas
- Risks / tradeoffs
- Suggested tests
- Recommendation: proceed / needs clarification first

## Prompt ví dụ

```text
Use ticket-planner for Jira ticket ML-39.
Based on the analysis, propose the implementation approach, affected areas, risks, and suggested tests before coding.
```
