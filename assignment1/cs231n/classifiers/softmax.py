import numpy as np
from random import shuffle
from past.builtins import xrange

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)
  
  num_data = X.shape[0]
  num_class = np.max(y)+1

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  for it in xrange(num_data):
        score = X[it].dot(W)
        score_max = np.max(score)
        score -= score_max
        prob = np.exp(score)/np.sum(np.exp(score))
        loss += -np.log(prob[y[it]])
        dW[:,y[it]]-=X[it]
        for jt in xrange(num_class):
            dW[:,jt]+= prob[jt]*X[it]
        
        
        
                
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################
  loss /= num_data
  dW /= num_data
  
  # Add regularization to the loss.
  loss += reg * np.sum(W * W)/2
  dW += reg * W
  
  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  num_data = X.shape[0]
  num_class = np.max(y)+1

  score = X.dot(W)
  score_max = np.max(score,axis=1)
  score -= np.reshape(score_max, [num_data,-1])
  score_norm = np.sum(np.exp(score), axis =1)
  score_norm = np.reshape(score_norm, [num_data,-1])
  prob = np.exp(score)/score_norm
  loss = np.sum(-np.log(prob[np.arange(num_data),y]))

  
  ind = np.zeros_like(prob)
  ind[np.arange(num_data),y] = 1
  dW +=X.T.dot(prob-ind)

  loss /= num_data
  dW /= num_data
  
  # Add regularization to the loss.
  loss += reg * np.sum(W * W)/2
  dW += reg * W
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW

