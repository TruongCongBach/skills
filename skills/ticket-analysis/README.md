# Ticket Analysis

`ticket-analysis` là skill đầu tiên nên dùng khi vừa nhận ticket.

## Dùng khi nào

- Khi cần đọc Jira ticket trước khi code
- Khi cần làm rõ expected vs actual behavior
- Khi có screenshot, HAR, Charles, zip log cần triage
- Khi cần quyết định ticket đã đủ rõ để implement chưa

## Không dùng khi nào

- Khi bạn đã hiểu rõ ticket và đang chọn hướng implement
- Khi bạn đã bắt đầu code
- Khi bạn cần review implementation hoặc commit

## Mục tiêu

- Hiểu đúng vấn đề
- Chỉ ra thông tin còn thiếu hoặc ambiguity
- Tóm tắt business impact, expected behavior, actual behavior
- Kết luận `ready to implement` hoặc `not yet ready`

## Input thường gặp

- Jira ticket
- Ticket comments
- Screenshot/design image
- HAR, Charles, zip logs

## Output mong đợi

- Ticket summary
- Problem statement
- Expected vs actual behavior
- Missing information
- Root-cause hypotheses
- Recommendation: ready / not ready

## Prompt ví dụ

```text
Use ticket-analysis for Jira ticket ML-39.
Read the ticket first, summarize the issue, identify missing information, and tell me whether this is ready for implementation.
```
