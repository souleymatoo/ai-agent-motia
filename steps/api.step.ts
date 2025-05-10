import { ApiRouteConfig, StepHandler } from 'motia'
import { z } from 'zod'

const inputSchema = z.object({})

export const config: ApiRouteConfig = {
  type: 'api',
  name: 'Sentiment Analysis Agent',
  description: 'Sentiment Analysis Agent',
  path: '/default',
  virtualSubscribes: ['/default'],
  method: 'POST',
  emits: ['product-review'],
  bodySchema: inputSchema,
  flows: ['default'],
}

export const handler: StepHandler<typeof config> = async (req, { logger, emit }) => {
  logger.info('processing API request', req)

  const review = 'This product is great! I love it!'
  const negativeReview = 'This product is terrible! I hate it!'

  await emit({
    topic: 'product-review',
    data: { "review": negativeReview },
  })

  return {
    status: 200,
    body: { message: 'product-review topic emitted' },
  }
}
