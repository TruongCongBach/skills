# Ticket Review

`ticket-review` dùng sau khi code đã được viết xong và cần so lại với ticket.

## Dùng khi nào

- Khi implementation đã có và cần review trước khi approve
- Khi cần so với Jira ticket, acceptance criteria, screenshot/design reference
- Khi cần check UX quality, missing states, test gaps, maintainability

## Không dùng khi nào

- Khi vẫn đang ở bước planning
- Khi chưa có code để review
- Khi mục tiêu là commit hoặc đóng ticket

## Mục tiêu

- Kiểm tra implementation có khớp ticket không
- Chỉ ra phần đúng, phần thiếu, phần mismatch
- Nêu missing states, UX risks, code quality concerns, test gaps
- Kết luận `ready` hoặc `needs revision`

## Input thường gặp

- Jira ticket
- Changed files / diff
- Screenshot/design image
- Existing analysis/planning context

## Output mong đợi

- What appears correctly implemented
- What appears incomplete
- Missing states
- UX risks
- Required changes
- Suggested correction order
- Final QA checklist

## Prompt ví dụ

```text
Use ticket-review for ML-39.
Review the implementation against the ticket and tell me what still needs revision before approval.
```
