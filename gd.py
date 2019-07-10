import numpy as np

class gd_pv_2d:
    
    def __init__(self, fn_loss, fn_grad):
        self.fn_loss = fn_loss
        self.fn_grad = fn_grad
        
    def find_min(self, x_init, n_iter, eta, tol):
        #self.x_init = x_init
        #self.n_iter = n_iter
        #self.eta = eta
        #self.tol = tol
        x = x_init
        
        loss_path = []
        x_path = []
        #x_path = np.zeros([n_iter+1,2])
        
        x_path.append(x)
        #x_path[0,:] = x
        loss_this = self.fn_loss(x[0],x[1])
        loss_path.append(loss_this)
        g = self.fn_grad(x[0],x[1])

        for i in range(n_iter):
            if abs(g[0]) < tol and abs(g[1]) < tol :
                break
            g = self.fn_grad(x[0],x[1])
            x[0] += -eta * g[0]
            x[1] += -eta * g[1]
            x = [x[0],x[1]]
            x_path.append(x)
            #x_path[i] = x
            loss_this = self.fn_loss(x[0],x[1])
            loss_path.append(loss_this)
            
        self.loss_path = loss_path
        self.x_path = x_path
        self.loss_fn_min = loss_this
        self.x_at_min = x
        self.n_iter = len(x_path)
    # Momentum 
    def momentum(self, x_init, n_iter, eta, tol, alpha):
        x = x_init

        loss_path = []
        x_path = []

        x_path.append(x)
        loss_this = self.fn_loss(x[0],x[1])
        loss_path.append(loss_this)
        g = self.fn_grad(x[0],x[1])
        nu = 0

        for i in range(n_iter):
            g = self.fn_grad(x[0],x[1])
            if np.abs(g[0]) < tol and np.abs(g[1]) < tol :
                break

            nu = alpha * nu + eta * g
            x[0] += -nu[0]
            x[1] += -nu[1]
            x = [x[0],x[1]]
            x_path.append(x)
            loss_this = self.fn_loss(x[0],x[1])
            loss_path.append(loss_this)
            
        if np.isnan(g[0]) or np.isnan(g[1]):
            print('Exploded')
        elif np.abs(g[0]) > tol or np.abs(g[1]) > tol:
            print('Did not converge')
        else:
            print('Converged in {} steps.  Loss fn {} achieved by x = {}'.format(i, loss_this, x))
            
        self.loss_path = np.array(loss_path)
        self.x_path = np.array(x_path)

    def nag(self, x_init, n_iter, eta, tol, alpha):
        x = x_init

        loss_path = []
        x_path = []

        x_path.append(x)
        loss_this = self.fn_loss(x[0],x[1])
        loss_path.append(loss_this)
        g = self.fn_grad(x[0],x[1])
        nu = 0

        for i in range(n_iter):
            # i starts from 0 so add 1
            # The formula for mu was mentioned by David Barber UCL as being Nesterovs suggestion
            mu = 1 - 3 / (i + 1 + 5) 
            temp = np.array(x) -  np.array(mu*nu)
            g = self.fn_grad(temp[0],temp[1])
            if (np.abs(g[0]) < tol and  np.abs(g[1]) < tol) or (np.isnan(g[0]) and np.isnan(g[1]) ):
                break

            nu = alpha * nu + eta * g
            x[0] += -nu[0]
            x[1] += -nu[1]
            x = [x[0],x[1]]
            x_path.append(x)
            loss_this = self.fn_loss(x[0],x[1])
            loss_path.append(loss_this)
            
        if np.isnan(g[0]):
            print('Exploded')
        elif np.abs(g[0]) > tol:
            print('Did not converge')
        else:
            print('Converged in {} steps.  Loss fn {} achieved by x = {}'.format(i, loss_this, x))
        self.loss_path = np.array(loss_path)
        self.x_path = np.array(x_path)

        self.loss_path = np.array(loss_path)
        self.x_path = np.array(x_path)